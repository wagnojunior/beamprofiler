# -*- coding: utf-8 -*-
"""
This module handles the extraction of the measured quantities in accordance
with the **ISO 13694** and **ISO 11145**.
"""

# =============================================================================
# Imports
# =============================================================================
import numpy as np


def max_power_density(raw_data):
    """
    `max_power_density` returns the maximum power density in the power density
    distribution. In order to avoid errors induced by background noise, it is
    recommended to use as input a noise-corrected dataframe.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.

    Returns
    -------
    float64
        maximum power density of the power density distribution.

    """
    # The first .max() returns the maximum value per each column, while the
    # second .max() returns the maximum value amount the maximums
    return raw_data.max().max()


def total_power(raw_data):
    """
    `total_power` returns the total power in the power density distribution. In
    order to avoid errors induced by background noise, it is recommended to
    use as input a noise-corrected dataframe.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution distribution.

    Returns
    -------
    float64
        total power of the power density distribution.

    """

    # Convert dataframe to numpy array
    raw_data_np = raw_data.to_numpy()

    return np.nansum(raw_data_np)


def clip_level_power_density(raw_data, clip_level):
    """
    `clip_level_power_density` returns a fraction of the maximum power density.
    In order to avoid errors induced by background noise, it is recommended to
    use as input a noise-corrected dataframe.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    clip_level : float
        0 <= clip_level <= 1.

    Returns
    -------
    float64
        fraction of the maximum power density.

    """

    return max_power_density(raw_data) * clip_level


def clip_level_power(raw_data, clip_level):
    """
    `clip_level_power` returns the total power in the filtered power density
    distribution. Only power densities that are greater than the clip-level
    power density are considered in the calculation. In order to avoid errors
    induced by background noise, it is recommended to use as input a
    noise-corrected dataframe.

    Parameters
    ----------
    raw_data : dataframe
        noise-corrected power density distribution.
    clip_level : float
        0 <= clip_level <= 1. The clip-level defines the clip-level power
        density, and only power densities greater than to this threshold value
        are considered in the calculation.

    Returns
    -------
    float64
        total power considering only power densities that are greater than a
        threshold.

    """
    # The threshold is defined as the clip-level power density
    threshold = clip_level_power_density(raw_data, clip_level)
    raw_data_np = raw_data[raw_data >= threshold]

    return np.nansum(raw_data_np)
