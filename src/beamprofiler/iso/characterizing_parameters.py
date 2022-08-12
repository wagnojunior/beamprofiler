# -*- coding: utf-8 -*-
"""
This module handles the calculation of the characterizing parameters in
accordance with the **ISO 13694** and **ISO 11145**.
"""

# =============================================================================
# Imports
# =============================================================================
import math
import numpy as np

from beamprofiler.iso import measured_quantities as mq
from beamprofiler.utils import data_processing as dp


def fractional_power(raw_data, clip_level):
    """
    `fractional_power` returns the fraction of the clip-level power to the
    total power. In order to avoid errors induced by background noise, it is
    recommended to use as input a noise-corrected dataframe.

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
        0 <= fractional_power <= 1. fractional_power = 1 for a perfect flat-top
        beam.

    """

    return (
        mq.clip_level_power(raw_data, clip_level) /
        mq.total_power(raw_data)
    )


def beam_center(raw_data, raw_header):
    """
    `beam_center` returns the center coordinate of the power density
    distribution. In order to avoid errors induced by background noise, it is
    recommended to use as input a noise-corrected dataframe. The beam center
    is defined as the first-order moment of the power density distribution.

    The center coordinate on the x-axis is defined as:
    M_1,0/M_0,0.
    The center coordinate on the y-axis is defined as
    M_0,1/M_0,0.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    raw_header : dataframe
        header of the power density distribution.

    Returns
    -------
    int
        center coordinate on the x-axis in pixel.
    int
        center coordinate on the y-axis in pixel.

    """

    m_0 = dp.image_moments(raw_data, raw_header, 0, 0, 0, 0)
    m_1x = dp.image_moments(raw_data, raw_header, 1, 0, 0, 0)
    m_1y = dp.image_moments(raw_data, raw_header, 0, 1, 0, 0)

    # Since this is a discrete function the values are rounded and converted
    # to int
    return (
        int(round(m_1x / m_0)),
        int(round(m_1y / m_0))
    )


def beam_width(raw_data, raw_header, beam_center_x, beam_center_y):
    """
    `beam_width` returns the beam width of the power density distribution. In
    order to avoid errors induced by background noise, it is recommended to use
    as input a noise-corrected dataframe. The beam width is defined as four
    times the square root of the second-order moment of the power density
    distribution about the beam center.


    The beam width about the x-axis is defined as:
    4*sqrt(M_2,0 - beam_center_x * M_1,0)
    The beam with about the y-axis is defined as:
    4*sqrt(M_0,2 - beam_center_y * M_0,1).


    Note that this definition comes from the mathematical manipulation and
    simplification of the formula applied in this function. For more
    information, refer to
    https://en.wikipedia.org/wiki/Image_moment#Central_moments

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    raw_header : dataframe
        header of the power density distribution.
    beam_center_x : int
        center coordinate of the power density distribution on the x-axis.
    beam_center_y : int
        center coordinate of the power density distribution on the y-axis.

    Returns
    -------
    float
        beam width about the x-axis in pixel.
    float
        beam width about the y-axis in pixel.

    """

    m_0 = dp.image_moments(raw_data, raw_header, 0, 0, 0, 0)
    m_2x = dp.image_moments(raw_data, raw_header, 2, 0, beam_center_x, 0)
    m_2y = dp.image_moments(raw_data, raw_header, 0, 2, 0, beam_center_y)

    try:
        return (
            round(4 * (math.sqrt(m_2x / m_0)), 4),
            round(4 * (math.sqrt(m_2y / m_0)), 4)
        )
    except ZeroDivisionError:
        return -1, -1


def beam_aspect_ratio(d_x, r_x, d_y, r_y):
    """
    `beam_aspect_ratio` returns the aspect ratio (circularity or squareness) of
    the power density distribution. The beam aspect ratio is defined as:
    beam_width_y / beam_width_x.

    If the pixel resolution about the x- and y-axis are the same, the aspect
    ratio can be calculated using the beam width in pixel or in millimeter.
    However, if the pixel resolution about the x- and y-axis are not the same,
    then the aspect ratio should be calculated using the beam width in
    millimeter. Therefore, this function converts the beam width from pixel to
    millimeter.

    Parameters
    ----------
    d_x : float
        beam width about the x-axis in pixel.
    r_x : float64
        pixel resolution on the x-axis in millimeter per pixel.
    d_y : float
        beam width about the y-axis in pixel.
    r_y : float64
        pixel resolution on the y-axis in millimeter per pixel.

    Returns
    -------
    float64
        beam aspect ratio.

    """

    return (d_y*r_y) / (d_x*r_x)


def clip_level_irradiation_area(raw_data, clip_level):
    """
    `clip_level_irradiation_area` returns the area of the filtered power
    density distribution in pixel. Only power densities that are greater than
    the clip-level power density are considered in the calculation. In order to
    avoid errors induced by background noise, it is recommended to use as input
    a noise-corrected dataframe.

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
    int64
        irradiation area considering only power densities that are greater than
        a threshold.

    """

    # The threshold is defined as the clip-level power density
    threshold = mq.clip_level_power_density(raw_data, clip_level)

    # The area is simply the count of pixels that satisfy the condition
    return raw_data[raw_data > threshold].count().sum()


def clip_level_average_power_density(clip_level_power,
                                     clip_level_irradiation_area):
    """
    `clip_level_average_power_density` returns the average power density of the
    filtered power density distribution.

    Parameters
    ----------
    clip_level_power : float64
        total power considering only power densities that are greater than a
        threshold.
    clip_level_irradiation_area : int64
        irradiation area considering only power densities that are greater than
        a threshold.

    Returns
    -------
    float64
        average power density of the filtered power density distribution.

    """

    # The average power density is defined as the power divided by the area
    return clip_level_power / clip_level_irradiation_area


def flatness_factor(clip_level_average_power_density, max_power_density):
    """
    `flatness_factor` returns the flatness factor of the power density
    distribution.

    The flatness factor is defined as the ratio of the clip-level average power
    density to the maximum power density. In other order, the flatness factor
    quantifies how much the average clip-level power density deviates from the
    maximum power density.

    Parameters
    ----------
    clip_level_average_power_density : float64
        average power density of the filtered power density distribution.
    max_power_density : float64
        maximum power density of the power density distribution.

    Returns
    -------
    flat64
        0 < flatness_factor <= 1. The flatness factor equals one for a
        perfectly flat-top power density distribution.

    """

    return clip_level_average_power_density / max_power_density


def beam_uniformity(raw_data, raw_header, clip_level_average_power_density,
                    clip_level_irradiation_area, clip_level_power_density):
    """
    `beam_uniformity` returns the beam uniformity of the power density
    distribution. In order to avoid errors induced by background noise, it is
    recommended to use as input a noise-corrected dataframe.

    The beam uniformity is defined as the normalized root mean square deviation
    of the power density distribution from its clip-level average power
    density.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    raw_header : dataframe
        header of the power density distribution.
    clip_level_average_power_density : flaot64
        average power density of the filtered power density distribution.
    clip_level_irradiation_area : int64
        irradiation area considering only power densities that are greater than
        a threshold.
    clip_level_power_density : float64
        fraction of the maximum power density.

    Returns
    -------
    aux : float64
        0 >= beam_uniformity. The beam uniformity equals zero for a perfectly
        flat-top power density distribution.

    """

    # Variable to keep the sum over the cells that meet the requirement
    aux_sum = 0

    # Convert input_data to numpy array
    raw_data_np = raw_data.to_numpy()

    # Subtract the clip level average power density
    aux = raw_data_np - clip_level_average_power_density

    # Power
    aux = aux**2

    # Loop through all cells in raw_data_pn
    for x in range(dp.get_xPixel(raw_header) - 1):

        for y in range(dp.get_yPixel(raw_header)):

            # Check if the current cell meets the threshold, which is the
            # clip level power density
            if raw_data_np[x][y] >= clip_level_power_density:

                # Sum
                aux_sum = aux_sum + aux[x][y]

    # Divide by the clip level irradiation area
    aux = aux_sum / clip_level_irradiation_area

    # Square root
    aux = np.sqrt(aux)

    # Divide by the clip level power density
    aux = aux / clip_level_average_power_density

    # Return
    return aux


def plateau_uniformity(raw_data, max_power_density, mix):
    """
    `platerau_uniformity` returns the plateau uniformity of the power density
    distribution. In order to avoid errors induced by background noise, it is
    recommended to use as input a noise-corrected dataframe.

    The power density histogram typically shows two peaks: one near the low-end
    of the x-axis and one near the high-end of the x-axis. The plateau
    uniformity is defined as the ratio of the full-width at half maximum (FWHM)
    of the high-end peak to the maximum power density.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    max_power_density : float64
        maximum power density of the power density distribution.
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

    # Approximation of the FWHM: 2.355 * std
    return full_width / max_power_density


def edge_steepness(clip_level_irradiation_area_1,
                   clip_level_irradiation_area_2):
    """
    `edge_steepness` returns the edge steepness of the power density
    distribution. The edge steepness is defined as the normalized difference
    between two clip-level irradiation areas, namely the clip-level irradiation
    area 1 (defined by the clip-level 1) and the clip-level irradiation area 2
    (defined by the clip-level 2).

    Note that clip-level 1 < clip-level 2, and consequently irradiation area 1
    > irradiation area 2.

    Parameters
    ----------
    clip_level_irradiation_area_1 : int64
        clip-level irradiation area defined by the clip-level 1.
    clip_level_irradiation_area_2 : int64
        clip-level irradiation area defined by the clip-level 2.

    Returns
    -------
    float64
        0 < edge_steepness < 1. The edge steepness equals zero for a power
        density distribution with perfectly vertical edges.

    """

    if clip_level_irradiation_area_1 < clip_level_irradiation_area_2:
        raise Exception("The clip-level irradiation 1 should be larger than \
                        the clip-level irradiation 2.")

    return (
        (clip_level_irradiation_area_1 - clip_level_irradiation_area_2) /
        clip_level_irradiation_area_1
    )
