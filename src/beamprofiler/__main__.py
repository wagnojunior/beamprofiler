# -*- coding: utf-8 -*-
"""
Main module of BeamProfiler.
"""

# =============================================================================
# Imports
# =============================================================================
from src.beamprofiler import analysis
import sys

if __name__ == '__main__':

    # Get arguments from the command line
    indir = sys.argv[1]
    fileName = sys.argv[2]
    eta = float(sys.argv[3])
    epsilon = float(sys.argv[4])
    mix = int(sys.argv[5])

    # Run
    analysis.run(indir, fileName, eta, epsilon, mix)
