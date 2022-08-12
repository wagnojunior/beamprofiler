# -*- coding: utf-8 -*-
"""
This module handles the data processing prior to the beam analysis.
"""

# =============================================================================
# Imports
# =============================================================================
import os
import pandas as pd
import numpy as np

from sklearn import mixture
from scipy import stats


def raw_data(fullPath):
    """
    `raw_data` returns the power density distribution.

    Parameters
    ----------
    fullPath : str
        full path to the .csv file that contains the power density
        distribution.

    Returns
    -------
    dataframe
        power density distribution.

    """

    # Check the file's extension
    ext = os.path.splitext(fullPath)[1]

    if ext == '.xls' or ext == '.xlsx':
        return pd.read_csv(fullPath, header=None, sep='\t', skiprows=1)
    elif ext == '.csv':
        return pd.read_csv(fullPath, header=None, sep=',', skiprows=1)


def raw_header(fullPath):
    """
    `raw_header` returns the header of the power density distribution. The
    header contains important information regarding the beam profiling, such as
    the measurement windows, number of pixels, null point, and so on.

    Parameters
    ----------
    fullPath : str
        full path to the .csv file that contains the power density
        distribution.

    Returns
    -------
    dataframe
        header of the power density distribution.

    """

    # Check the file's extension
    ext = os.path.splitext(fullPath)[1]

    if ext == '.xls' or ext == '.xlsx':
        return pd.read_csv(fullPath, header=None, sep='\t', nrows=1)
    elif ext == '.csv':
        return pd.read_csv(fullPath, header=None, sep=',', nrows=1)


def remove_background(raw_data, raw_header):
    """
    `remove_background` returns the noise-corrected power density distribution.
    Background noise and digitizer baseline are known to negatively affect the
    soundness of the beam analysis. Therefore, a noise correction method must
    be applied before carrying on the calculations.

    ISO 13694 defines two background correction methods based on the dark-field
    map of the detector:
    1) Background map subtraction: the background map is subtracted from the
    power density distribution pixel by pixel.
    2) Average background map subtraction: the average background map is
    subtracted from the power density distribution.

    This method implements option 2), and the average background map is
    retrieved from the header.

    Parameters
    ----------
    raw_data : dataframe
        power density distribution.
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    dataframe
        noise corrected power density distribution.

    """

    # get_nullPoint returns the null point, that is the average background map
    return raw_data - get_nullPoint(raw_header)


def get_nullPoint(raw_header):
    """
    `get_nullPoint` returns the average background map for noise correction.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    float64
        null point, that is the average background map.

    """

    return raw_header.iloc[0][17]


def get_xWindow(raw_header):
    """
    `get_xWindow` returns the measurement window size on the x-axis in
    millimeter. Depending on the arrangement of the measurement setup, the
    x-axis of the detector and of the dataframe may not match.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    float64
        measurement window size on the x-axis in millimeter.

    """

    return raw_header.iloc[0][14]


def get_yWindow(raw_header):
    """
    `get_yWindow` returns the measurement window size on the y-axis in
    millimeter. Depending on the arrangement of the measurement setup, the
    y-axis of the detector and of the dataframe may not match.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    float64
        measurement window size on the y-axis in millimeter.

    """

    return raw_header.iloc[0][11]


def get_xPixel(raw_header):
    """
    `get_xPixel` returns the number of pixels on the x-axis. Depending on the
    arrangement of the measurement setup, the x-axis of the detector and of the
    dataframe may not match.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    int64
        the number of pixels on the x-axis.

    """

    return raw_header.iloc[0][5]


def get_yPixel(raw_header):
    """
    `get_yPixel` returns the number of pixels on the y-axis. Depending on the
    arrangement of the measurement setup, the y-axis of the detector and of the
    dataframe may not match.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    int64
        the number of pixels on the y-axis.

    """

    return raw_header.iloc[0][8]


def get_xResolution(raw_header):
    """
    `get_xResolution` returns the pixel resolution on the x-axis in millimeter
    per pixel. The pixel resolution is calculated by dividing the windows size
    on the x-axis by the number of pixels on the x-axis.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    float64
        pixel resolution about the x-axis in millimeter per pixel.

    """

    return get_xWindow(raw_header) / get_xPixel(raw_header)


def get_yResolution(raw_header):
    """
    `get_yResolution` returns the pixel resolution on the y-axis in millimeter
    per pixel. The pixel resolution is calculated by dividing the windows size
    on the y-axis by the number of pixels on the y-axis.

    Parameters
    ----------
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    float64
        pixel resolution about the y-axis in millimeter per pixel.

    """

    return get_yWindow(raw_header) / get_yPixel(raw_header)


def image_moments(raw_data, raw_header, p, q, x0, y0):
    """
    `image_moments` returns the nth-order of the power density distribution.
    According to Wikipedia, "In image processing, computer vision and related
    fields, an image moment is a certain particular weighted sum (moment) of
    the image pixels' intensities, or a function of such moments, usually
    chosen to have some attractive property or interpretation."

    The zeroth-order moment is the unweighted sum of the power density
    distribution. The first-order moment is the sum of each pixel weighted by
    its corresponding column index (if the moment is calculated about the
    x-axis) and by its corresponding row index (if the moment is calculated
    about the y-axis).

    M_p,q = sum_x[sum_y[(x-x0)^p * (y-y0)^q * f(x, y)]] is the image moment of
    order p and reference point x0 on the x-axis and of order q and reference
    point y0 on the y-axis.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    raw_header : dataframe
        header of the power density distribution.
    p : int
        moment order on the x-axis.
    q : int
        moment order on the y-axis.
    x0 : int/float64
        reference point on the x-axis.
    y0 : int/float64
        reference point on the y-axis.

    Returns
    -------
    aux : float64
        moment of order p and reference point x0 on the x-axis and of order q
        and reference point y0 on the y-axis.

    """

    aux = 0

    # Convert input_data to numpy array
    raw_data_np = raw_data.to_numpy()

    # Iterate through all columns and rows
    for x in range(get_xPixel(raw_header) - 1):

        for y in range(get_yPixel(raw_header) - 1):

            # Apply formula
            aux = aux + (((x - x0)**p) * ((y - y0)**q) * raw_data_np[x][y])

    return aux


def normal_mixture(df, mix):
    """
    `normal_mixture` returns the normal mixture fit.

    Parameters
    ----------
    df : dataframe
        data to which the normal mixture will be fitted.
    mix : int
        number of normal mixtures. mix = [1, 2, 3]

    Raises
    ------
    Exception
        in case the number of mixtures of not 1, 2, or 3.

    Returns
    -------
    x : array of float64
        x-axis component of the normal mixture fit.
    y : array of float64
        y-axis component of the normal mixture fit.

    """

    # Convert the filtered dataframe to a 1d numpy array (excluding the NaN)
    array = df.values.flatten()
    array = array[np.logical_not(np.isnan(array))]

    # Filter the array to get only values located at the high-end of the
    # x-axis. The higher the cut-off percentage value, the more data is
    # filtered out
    cut_off = (array.max() - array.min()) * 0.5
    array = array[array >= cut_off]

    # Reshape the raw data for Normal Mixture Fit
    array = array.reshape(-1, 1)

    # Curve fitting
    gmm = (
        mixture.GaussianMixture(n_components=mix,
                                max_iter=1000,
                                covariance_type='full')
        .fit(array)
    )

    # Get the mean and std of gmm
    mean = gmm.means_
    std = np.sqrt(gmm.covariances_)
    prob = gmm.weights_

    # Create the x-axis for the curve fitting
    x = np.linspace(array.min(), array.max(), 10000)

    # Calculates the normal mixture based on the specified number of mix
    if mix == 3:
        y_3 = stats.norm.pdf(x, mean[2], std[2][0][0])*prob[2]
        y_2 = stats.norm.pdf(x, mean[1], std[1][0][0])*prob[1]
        y_1 = stats.norm.pdf(x, mean[0], std[0][0][0])*prob[0]
    elif mix == 2:
        y_3 = 0
        y_2 = stats.norm.pdf(x, mean[1], std[1][0][0])*prob[1]
        y_1 = stats.norm.pdf(x, mean[0], std[0][0][0])*prob[0]
    elif mix == 1:
        y_3 = 0
        y_2 = 0
        y_1 = stats.norm.pdf(x, mean[0], std[0][0][0])*prob[0]
    else:
        raise Exception("The number of mixtures should be 1, 2, or 3.")

    # Add the three normal mixtures
    y = y_1 + y_2 + y_3

    return x, y


def pre_top_hat(raw_data):
    """
    `pre_top_hat` returns a dataframe with the necessary data to calculate the
    top-hat factor and to plot the normalized energy curve.

    Parameters
    ----------
    raw_data : dataframe
        power density distribution.

    Returns
    -------
    df : dataframe
        necessary data to calculate the top-hat factor and to plot the
        normalized energy curve.

    """

    # Stack raw_data into a single column
    raw_data_stacked = raw_data.stack(level=-1, dropna=True)

    # Get the histogram count for each bin and sort the index
    hist = raw_data_stacked.value_counts().sort_index()

    # Finds the lower_limit, which is the intensity value (bin) with the
    # highest count
    lower_limit = hist.idxmax()

    # Creates a new data frame using <hist>
    df = pd.DataFrame(data={'Count': hist}, index=hist.index)

    # Add column <Energy> having the bin with highest count (<lower_limit>)
    # as zero
    df['Energy'] = df['Count'] * (df.index - lower_limit)

    # Because the bin with the highest count is set to zero, some energy values
    # are negative, therefore should be removed
    df = df[(df >= 0).all(axis=1)]

    # Since not all bins have a count, fill missing values with zeros
    df = (
        df.reindex(np.arange(min(df.index), max(df.index)+1), fill_value=0)
    )

    # Add reverse cumulative sum
    df['Cumulative Energy'] = (
        df.loc[::-1, 'Energy'].cumsum()[::-1]
    )

    # Add normalized cumulative sum
    df['Normalized Cumulative Energy'] = (
        100*df['Cumulative Energy'].to_numpy() /
        df.max(axis=0)['Cumulative Energy']
    )

    # Add normalized intensity
    df['Normalized Intensity'] = (
        100*(df.index - min(df.index))/(max(df.index) - min(df.index))
    )

    return df
