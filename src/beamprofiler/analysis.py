# -*- coding: utf-8 -*-
"""
This module handles the main operation of the beam analysis.
"""

# =============================================================================
# Imports
# =============================================================================
import sys

from beamprofiler import beam
from beamprofiler.utils import report, plot


def run(path, fileName, eta, epsilon, mix, **kwargs):
    """
    `run` runs the beam analysis.

    Parameters
    ----------
    path : str
        path to the power density distribution file.
    fileName : str
        name of the power density distribution file.
    eta : float
        upper clip-level. 0 < eta < 1.
    epsilon : float
        lower clip-level. o < epsilon < 1.
    mix : int
        number of normal mixtures used in the curve fitting. mix = [1, 2, 3].

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

    # Creates an instance of Beam
    myBeam = beam.Beam(path, fileName, eta, epsilon, mix)

    # Plots
    plot.run(path, fileName, myBeam, **kwargs)

    # Generates the report
    report.write(path, fileName, myBeam)


if __name__ == '__main__':

    # Get arguments from the command line
    path = sys.argv[1]
    fileName = sys.argv[2]
    eta = float(sys.argv[3])
    epsilon = float(sys.argv[4])
    mix = int(sys.argv[5])

    # Run
    run(path, fileName, eta, epsilon, mix)
