# -*- coding: utf-8 -*-
"""
This module handles the main operation of the beam analysis.
"""

# =============================================================================
# Imports
# =============================================================================
import sys

from src.beamprofiler import beam
from src.beamprofiler.utils import report, plot


def run(path, fileName, eta, epsilon, mix, **kwargs):
    """
    `run` runs the beam analysis.

    Parameters
    ----------
    path : str
        full path to the power density distribution file.
    fileName : str
        file name the power density distribution.
    eta : float
        upper clip-level. 0 < eta < 1.
    epsilon : float
        lower clip-level. o < epsilon < 1.
    mix : int
        number of normal mixtures used in the curve fitting. mix = [1, 2, 3].
    **kwargs : dict
        optional keyword arguments. For more information, please see `utils.
        plot.histogram

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
