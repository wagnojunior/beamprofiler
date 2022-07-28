# -*- coding: utf-8 -*-
"""
This module handles the calculation of the characterizing parameters in
accordance with non-ISO definitions.
"""

# =============================================================================
# Imports
# =============================================================================
import numpy as np
from scipy import stats

from src.beamprofiler.iso import measured_quantities as mq
from src.beamprofiler.utils import data_processing as dp


def plateau_uniformity(raw_data, mix):
    """
    `platerau_uniformity` returns the plateau uniformity of the power density
    distribution. In order to avoid errors induced by background noise, it is
    recommended to use as input a noise-corrected dataframe.

    The power density histogram typically shows two peaks: one near the low-end
    of the x-axis and one near the high-end of the x-axis. The plateau
    uniformity is defined as the ratio of the full-width at half maximum (FWHM)
    of the high-end peak to the energy density value corresponding to the
    maximum.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    mix : int
        mix = [1, 2, 3]. `mix` is the number of normal mixtures used in the
        data fitting.

    Returns
    -------
    float64
        0 < plateau_uniformity < 1. The plateau uniformity equals zero for a
        perfectly flat-top power density distribution.

    """

    x, y = dp.normal_mixture(raw_data, mix)

    # Calculates the full width at half maximum. The half_max part is quite
    # straight forward: simply divide the maximum by 2. The full_width part
    # is calculated by getting the size of <y> that is greater or equal
    # than <half_max> and then multiplying by the step size of <x>
    half_max = y.max()/2
    full_width = np.where(y >= half_max)[0].size * (x[1]-x[0])

    # Get the index of the maximum value and the corresponding energy density
    power_density_max = x[np.argmax(y)]

    # Approximation of the FWHM: 2.355 * std
    return full_width / power_density_max


def clip_level_beam_width(raw_data, clip_level):
    """
    `clip_level_beam_width` returns the clip-level beam width of the filtered
    power density distribution in pixel. Only power densities that are greater
    than the clip-level power density are considered in the calculation. In
    order to avoid errors induced by background noise, it is recommended to use
    as input a noise-corrected dataframe.

    The clip-level beam width is defined as the count of pixels that have a
    power density greater than the clip-level power density. The clip-level
    beam width about the x axis is computed by iterating along the row indices
    and the clip-level beam width about the y axis is computed by iterating
    along the column indices. The results for each axis are then averaged out
    disregarding the zeros and any eventual outliers.

    The use of a high-pixel resolution is recommended in order to avoid
    quantization errors that may arise from counting pixels. Transpose raw_data
    to get the result along the x-axis.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    clip_level : float
        0 <= clip_level <= 1. The clip-level defines the clip-level power
        density, and only power densities greater than this threshold value
        are considered in the calculation.

    Returns
    -------
    float64
        clip-level beam width of the filtered power density distribution in
        pixel.

    """

    # Threshold power density
    threshold = mq.clip_level_power_density(raw_data, clip_level)

    # Transpose raw_data to get the result along the x-axis
    beam_width = (raw_data > threshold).apply(np.count_nonzero)

    # Remove zero values
    beam_width = beam_width[beam_width > 0]

    # Filter out outliers 2 times
    for i in range(2):

        # Identify the outliers by calculating the z-score
        zScore = np.abs(stats.zscore(beam_width))

        # Check if zScore is filled with NaN (in case beam_width is filled
        # with the same values)
        # A RunTimeWarning is thrown when this condition is met
        if np.isnan(zScore).any():

            # If yes, then fill zScore with the value 1
            np.nan_to_num(zScore, copy=False, nan=1)

        # Get only values that have a z-score of less than or equal to 2
        beam_width = beam_width[zScore <= 1]

        # Check if edge_width is empty (in case of a perfect distribution)
        if beam_width.size == 0:

            # If yes, then add one entry equals to zero
            beam_width[0] = 0

            break

    # Return the average clip-level beam width
    return np.average(beam_width)


def clip_level_edge_width(raw_data, clip_level_1, clip_level_2):
    """
    `clip_level_edge_width` returns the clip-level edge width of the filtered
    power density distribution in pixel. Only power densities that are greater
    than the clip-level power density are considered in the calculation. In
    order to avoid errors induced by background noise, it is recommended to use
    as input a noise-corrected dataframe.

    The clip-level edge width is defined as the count of pixels that have a
    power density greater than the clip-level power density 1 (defined by the
    clip-level 1) AND lower than the clip-level power density 2 (defined by the
    clip-level 2). The clip-level edge width about the x-axis is computed by
    iterating along the row indices and the clip-level beam width about the
    y-axis is computed by iterating along the column indices. The results for
    each axis are then averaged out disregarding the zeros and any eventual
    outliers.

    The use of a high-pixel resolution is recommended in order to avoid
    quantization errors that may arise from counting pixels. Note that
    clip_level_1 < clip_level 2. Transpose raw_data to get the result along the
    x-axis.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    clip_level_1 : int64
        0 <= clip_level_1 <= 1. The clip-level defines the clip-level power
        density, and only power densities greater than this threshold value
        are considered in the calculation.
    clip_level_2 : TYPE
        0 <= clip_level_2 <= 1. The clip-level defines the clip-level power
        density, and only power densities less than this threshold value
        are considered in the calculation.

    Returns
    -------
    float64
        clip-level edge width of the filtered power density distribution in
        pixel.

    """

    # Threshold power density LOW value
    threshold_1 = mq.clip_level_power_density(raw_data, clip_level_1)

    # Threshold power density HIGH value
    threshold_2 = mq.clip_level_power_density(raw_data, clip_level_2)

    # Transpose raw_data to get the result along the x-axis
    edge_width = (
        ((raw_data > threshold_1) & (raw_data < threshold_2))
        .apply(np.count_nonzero)
    )

    # Remove zero values
    edge_width = edge_width[edge_width > 0]

    # Filter out outlilers 2 times
    for i in range(2):

        # Identify the outliers by calculating the z-score
        zScore = np.abs(stats.zscore(edge_width))

        # Check if zScore is filled with NaN (in case beam_width is filled
        # with the same values)
        # A RunTimeWarning is thrown when this condition is met
        if np.isnan(zScore).any():

            # If yes, then fill zScore with the value 1
            np.nan_to_num(zScore, copy=False, nan=1)

        # Get only values that have a z-score of less than or equal to 2
        edge_width = edge_width[zScore <= 1]

        # Check if edge_width is empty (in case of a perfect distribution)
        if edge_width.size == 0:

            # If yes, then add one entry equals to zero
            edge_width[0] = 0

            break

    # Return the average clip-level beam width
    return np.average(edge_width) / 2


def top_hat_factor(df):
    """
    `top_hat_factor` returns the top-hat factor of the normalized energy curve,
    which is generated from the power density distribution. In order to avoid
    errors induced by background noise, it is recommended to use as input a
    noise-corrected dataframe.

    Parameters
    ----------
    df : dataframe
        dataframe that contains, amoung other thinds, the normalized cumulative
        energy.

    Returns
    -------
    thf : float
        top-hat factor.

    """

    # Get the x-axis step of the normalized energy curve. Because this curve
    # curve is normalized, the length is 100 and therefore the step is 100
    # divided by the length of the data
    step = 100 / len(df)

    # Get the total sum from the normalized energy fraction
    total_sum = df.sum()['Normalized Cumulative Energy'] * step

    # The top-hat factor is the ratio of the total area (100 * 100) to the
    # area under the normalized energy curve. Multiply by 100 to get the
    # percentage value
    thf = total_sum / (10000)

    return thf
