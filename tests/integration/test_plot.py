# -*- coding: utf-8 -*-
"""
Test file for a real top-hat beam.
"""
import os
# =============================================================================
# Imports
# =============================================================================
import unittest

import pkg_resources

import beamprofiler


class TestFile(unittest.TestCase):
    """Extends the `unittest.TestCase` with a custom assertion"""
    
    def assertIsFile(self, path):
        """`assertIsFile` tests is the given path is a file"""
        
        if not os.path.isfile(path):
            raise AssertionError("File does not exists: %s" % str(path))


class TestPlot(TestFile):
    """Tests for file generation."""

    def setUp(self):
        """`setUp` sets up the test fixtures."""

        self.path = pkg_resources.resource_filename(__name__, "fixtures")
        self.fileName = 'lab_beam.xls'
        self.eta = 0.8
        self.epsilon = 0.1
        self.mix = 1
        self.beam = (
            beamprofiler.beam.Beam(self.path, self.fileName, self.eta,
                                   self.epsilon, self.mix)
        )
        
    def test_histogram(self):
        """`test_histogram` tests the histogram plot generation."""

        beamprofiler.utils.plot.histogram(self.path, self.fileName, self.beam)
        self.assertIsFile(
            os.path.join(self.path,
                         os.path.splitext(self.fileName)[0] +
                         " - histogram.png"))
        
    def test_heatmap2D(self):
        """`test_heatmap2D` tests the 2D heatmap plot generation."""

        beamprofiler.utils.plot.heat_map_2d(self.path, self.fileName, self.beam)
        self.assertIsFile(
            os.path.join(self.path,
                         os.path.splitext(self.fileName)[0] +
                         " - 2d heat map.png"))
        
    def test_heatmap3D(self):
        """`test_heatmap2D` tests the 2D heatmap plot generation."""

        beamprofiler.utils.plot.heat_map_3d(self.path, self.fileName, self.beam)
        self.assertIsFile(
            os.path.join(self.path,
                         os.path.splitext(self.fileName)[0] +
                         " - 3d heat map.png"))

    def test_normEnergyCurve(self):
        """`test_heatmap2D` tests the 2D heatmap plot generation."""

        beamprofiler.utils.plot.norm_energy_curve(self.path, self.fileName,
                                                  self.beam)
        self.assertIsFile(
            os.path.join(self.path,
                         os.path.splitext(self.fileName)[0] +
                         " - 3d heat map.png"))        
        

if __name__ == '__main__':
    unittest.main()
