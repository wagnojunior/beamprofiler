# -*- coding: utf-8 -*-
"""
This module handles the generation of the auxiliary plots.
"""

# =============================================================================
# Imports
# =============================================================================
import os
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.patches as mpatches
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter)

from mpl_toolkits.axes_grid1 import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes, mark_inset

from src.beamprofiler.utils import data_processing as dp


def general_plot():
    """
    `general_plot` returns a general-purpose, blank pyplot graph.

    Returns
    -------
    fig : Figure object of matplotlib.figure module
        blank matplotlib figure object.
    ax : AxesSubplot object of matplotlib.axes_subplots module
        blank matplotlib axes object.

    """

    golden_ratio = 1.618033988749895

    # Set global font style and size
    plt.rc('font', family='serif')
    plt.rcParams.update({'font.size': 6})

    fig = plt.figure(figsize=(5, 5 / golden_ratio), dpi=100)
    ax = fig.add_subplot(1, 1, 1)

    return fig, ax


def histogram(path, fileName, beam, **kwargs):
    """
    `histogram` plots the histogram of the power density distribution and the
    normal mixture fit of the top 40% of the range.

    Parameters
    ----------
    path : std
        path to where the graph will be saved.
    beam : Beam
        instance of type Beam.

    Other Parameters
    ----------------
    n_bins : int
        number of bins used in the histogram.
    zoom : float
        zoom of the inset image.
    x1 : float
        lower bound of the inset image on the x-axis.
    x2 : float
        upper bound of the inset image on the y-axis.
    y1 : float
        lower bound of the inset image on the y-axis.
    y2 : float
        upper bound of the inset image on the x-axis.

    Returns
    -------
    None.

    """

    # Check if any default value has been redefined in kwargs
    n_bins = kwargs.pop('bins', 256)
    zoom = kwargs.pop('zoom', 2)
    x1 = kwargs.pop('x1', 1600)
    x2 = kwargs.pop('x2', 2000)
    y1 = kwargs.pop('y1', 0)
    y2 = kwargs.pop('y2', 5000)

    # Get the figure and axes objects
    fig, ax = general_plot()

    # Add title and axis titles
    ax.set_title('Histogram Analysis', loc='center', pad=None)
    ax.set_xlabel('Power Density (ADC/px)')
    ax.set_ylabel('Number of counts')

    # Histogram
    array = beam.raw_data_null.to_numpy().flatten()
    hist, bins, bars = ax.hist(array, bins=n_bins, alpha=1, align='right',
                               histtype='stepfilled', label='Histogram')

    # Add an inset image
    inset = zoomed_inset_axes(ax, zoom=zoom, loc=1)
    inset.hist(array, bins=n_bins, alpha=1, histtype='stepfilled',
               align='right', label='Histogram')
    inset.set_xlim(x1, x2)
    inset.set_ylim(y1, y2)
    inset.tick_params(labelleft=False, labelbottom=False)
    mark_inset(ax, inset, loc1=3, loc2=3, fc="none", ec="0.5")

    # Get the highest histogram peak around the high-poewr density area (upper
    # 40% of the number of bins)
    low_bound = int(n_bins * 0.6)
    high_bound = n_bins
    max_count = max(hist[low_bound:high_bound])
    pdf_x, pdf_y = dp.normal_mixture(beam.raw_data_null, beam.mix)
    pdf_y = max_count * (pdf_y / pdf_y.max())
    inset.plot(pdf_x, pdf_y, 'k--', linewidth=0.7)

    # Now that the fit has been generated, it can be added to the main graph
    ax.plot(pdf_x, pdf_y, 'k--', linewidth=0.35)

    # Save and show
    fileName = os.path.splitext(fileName)[0]
    plt.savefig(os.path.join(path, fileName + ' - histogram.png'),
                bbox_inches='tight', dpi=300)
    plt.show()


def heat_map(path, fileName, beam, **kwargs):
    """
    `heat_map` plots the heat map of the power densidty distribution.

    Parameters
    ----------
    path : str
        path to where the graph will be saved..
    beam : Beam
        instance of type `Beam`.

    Other Parameters
    ----------------
    z_lim : float
        upper intensity limite of the cross-section graph of the power density
        distribution.
    cross_x : float
        x-coordinate of the cross-section graph of the power density
        distribution
    cross_y : float
        y-coordinate of the cross-section graph of the power density
        distribution

    Returns
    -------
    None.

    """

    # Check if any default value has been redefined in kwargs
    z_lim = kwargs.pop('z_lim', -1)
    cross_x = kwargs.pop('cross_x', beam.centerX * beam.xResolution)
    cross_y = kwargs.pop('cross_y', beam.centerY * beam.yResolution)

    # Get the figure and axes objects
    fig, main_ax = general_plot()

    # Create and configure the axes
    divider = make_axes_locatable(main_ax)

    # Right ax
    right_ax = divider.append_axes("right", 0.6, pad=0.2, sharey=main_ax)
    right_ax.yaxis.set_tick_params(labelleft=False)
    right_ax.set_xlabel('Intensity')
    if z_lim != -1:
        right_ax.set_xlim(right=z_lim)

    # Top ax
    top_ax = divider.append_axes("top", 0.6, pad=0.2, sharex=main_ax)
    top_ax.xaxis.set_tick_params(labelbottom=False)
    top_ax.set_ylabel('Intensity')
    if z_lim != -1:
        top_ax.set_ylim(top=z_lim)

    # Configure and plot main graph
    z = beam.raw_data.to_numpy()
    main_ax.imshow(z,
                   extent=(0,
                           dp.get_xWindow(beam.raw_header),
                           0,
                           dp.get_yWindow(beam.raw_header)),
                   interpolation='nearest',
                   cmap=cm.gist_rainbow_r,
                   origin='lower')
    main_ax.axvline(cross_x, color='k', linestyle="--", lw=0.8)
    main_ax.axhline(cross_y, color='k', linestyle="-", lw=0.8)
    main_ax.set_xlabel('x-axis (mm)')
    main_ax.set_ylabel('y-axis (mm)')

    # Create and configure the right sub ax
    y = np.mgrid[0:dp.get_yWindow(beam.raw_header):beam.yResolution]
    slice_y = 0
    try:
        # Data along the y-axis at the x-position defined by cross_x
        slice_y = (
            z[:, int(np.around(cross_x/beam.xResolution))]
        )
    except IndexError:
        print("Slice position is outside of the range. Please, check the "
              "slice position.")
    right_ax.plot(slice_y, y, color='k', linestyle="--", lw=0.5)

    # Create and configure the top sub ax
    x = np.mgrid[0:dp.get_xWindow(beam.raw_header):beam.xResolution]
    slice_x = 0
    try:
        # Data along the x-axis at the y-position defined by cross_y
        slice_x = (
            z[int(np.around(cross_y/beam.yResolution)), :]
        )
    except IndexError:
        print("Slice position is outside of the range. Please, check the "
              "slice position.")
    top_ax.plot(x, slice_x, color='k', linestyle="-", lw=0.5)

    # Save and show
    fileName = os.path.splitext(fileName)[0]
    plt.savefig(os.path.join(path, fileName + ' - heat map.png'),
                bbox_inches='tight', dpi=300)
    plt.show()


def norm_energy_curve(path, fileName, beam):

    # Get the figure and axes objects
    fig, ax = general_plot()

    df = dp.pre_top_hat(beam.raw_data)

    # Plot
    x = df['Normalized Intensity']
    y = df['Normalized Cumulative Energy']
    ax.plot(x, y, ls='-', color='blue', linewidth=0.5)

    # Fill area under the curve
    ax.fill_between(x, y, 0, color='blue', alpha=0.5)
    ax.fill_between(x, y, 100, color='gray', alpha=0.5)

    # x-axis
    ax.set_xlabel('Normalized Intensity (%)')
    plt.xlim(0, 100)
    ax.xaxis.set_major_locator(MultipleLocator(10))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.xaxis.set_minor_locator(MultipleLocator(5))
    ax.xaxis.set_tick_params(width=0.5)

    # y-axis
    ax.set_ylabel('Normalized Cumulative Energy (%)')
    plt.ylim(0, 100)
    ax.yaxis.set_major_locator(MultipleLocator(10))
    ax.yaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.yaxis.set_tick_params(width=0.5)

    ax.spines['top'].set_linewidth(0.5)
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['right'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)

    # Title
    plt.title('Energy curve', fontdict=None, loc='center', pad=None)

    # Legend
    blue_patch = (
        mpatches.Patch(color='blue', alpha=0.5,
                       label=str(round(beam.topHatFactor*100, 2))+'%')
    )
    gray_patch = (
        mpatches.Patch(color='gray', alpha=0.5,
                       label=str(round(100-beam.topHatFactor*100, 2))+'%')
    )
    ax.legend(handles=[blue_patch, gray_patch], loc='lower left')

    # Save and show
    fileName = os.path.splitext(fileName)[0]
    plt.savefig(os.path.join(path, fileName + ' - top-hat factor.png'),
                bbox_inches='tight', dpi=300)
    plt.show()


def run(path, fileName, beam, **kwargs):
    """
    `run` runs all the auxiliary plots.

    Parameters
    ----------
    path : str
        path where the graphs will be saved.
    beam : Beam
        instance of type `Beam`.
    **kwargs : dict
        optional keyword arguments. For more information, please see `utils.
        plot.histogram` and `utils.plot.heat_map`

    Returns
    -------
    None.

    """

    histogram(path, fileName, beam, **kwargs)
    heat_map(path, fileName, beam, **kwargs)
    norm_energy_curve(path, fileName, beam)
