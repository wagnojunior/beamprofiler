# -*- coding: utf-8 -*-
"""
Test file for a real top-hat beam.
"""
# =============================================================================
# Imports
# =============================================================================
import unittest
import pkg_resources

from beamprofiler import beam


class TestLab(unittest.TestCase):
    """Tests for a real top-hat beam."""

    def setUp(self):
        """`setUp` sets up the test fixtures."""

        path = pkg_resources.resource_filename(__name__,
                                               "fixtures")
        fileName = 'lab_beam.xls'
        eta = 0.8
        epsilon = 0.1
        mix = 1
        self.beam = (
            beam.Beam(path, fileName, eta, epsilon, mix)
        )

    def test_totalPower(self):
        """`test_totalPower` tests the total power."""

        self.assertEqual(self.beam.totalPower, 56487140.23199999)

    def test_power_eta(self):
        """`test_power_eta` tests the clip-level power."""

        self.assertEqual(self.beam.power_eta, 52701367.24899999)

    def test_maxPowerDensity(self):
        """`test_maxPowerDensity` tests the maximum power density."""

        self.assertEqual(self.beam.maxPowerDensity, 1922.937)

    def test_powerDensity_eta(self):
        """`test_powerDensity_eta` tests the clip-level power density."""

        self.assertEqual(self.beam.powerDensity_eta, 1538.3496)

    def test_averagePowerDensity_eta(self):
        """`test_averagePowerDensity_eta` tests the clip-level average power
        density."""

        self.assertEqual(self.beam.averagePowerDensity_eta, 1793.9669554072912)

    def test_centerX(self):
        """`test_centerX` tests the center coordinate on the x-axis."""

        self.assertEqual(self.beam.centerX, 132)

    def test_centerY(self):
        """`test_centerY` tests the center coordinate on the y-axis."""

        self.assertEqual(self.beam.centerY, 128)

    def test_widthX(self):
        """`test_widthX` tests the beam width about the x-axis."""

        self.assertEqual(self.beam.widthX, 186.1258)

    def test_widthY(self):
        """`test_widthY` tests the beam width about the y-axis."""

        self.assertEqual(self.beam.widthY, 227.3874)

    def test_irradiationArea_epsilon(self):
        """`test_irradiationArea_epsilon` tests the lower clip-level
        irradiation area."""

        self.assertEqual(self.beam.irradiationArea_epsilon, 33545)

    def test_irradiationArea_eta(self):
        """`test_irradiationArea_eta` tests the upper clip-level irradiation
        area."""

        self.assertEqual(self.beam.irradiationArea_eta, 29377)

    def test_aspectRatio(self):
        """`test_aspectRatio` tests the beam aspect ratio."""

        self.assertEqual(self.beam.aspectRatio, 1.2216866227035694)

    def test_fractionalPower_eta(self):
        """`test_fractionalPower_eta` tests the clip-level fractional power."""

        self.assertEqual(self.beam.fractionalPower_eta, 0.9329799142344374)

    def test_flatnessFactor_eta(self):
        """`test_flatnessFactor_eta` tests the clip-level flatness factor."""

        self.assertEqual(self.beam.flatnessFactor_eta, 0.9329306968492942)

    def test_beamUniformity_eta(self):
        """`test_beamUniformity_eta` tests the clip-level beam uniformity."""

        self.assertEqual(self.beam.beamUniformity_eta, 0.0182239335908005)

    def test_plateauUniformity_eta(self):
        """`test_plateauUniformity_eta` tests the clip-level plateau
        uniformity."""

        self.assertEqual(self.beam.plateauUniformity_eta, 0.15119141872942682)

    def test_edgeSteepness_eta(self):
        """`test_edgeSteepness_eta` tests the clip-level edge steepness."""

        self.assertEqual(self.beam.edgeSteepness_eta, 0.12425100611119391)

    def test_widthX_eta(self):
        """`test_widthX_eta` tests the clip-level beam width about the
        x-axis."""

        self.assertEqual(self.beam.widthX_eta, 154.0)

    def test_widthY_eta(self):
        """`test_widthY_eta` tests the clip-level beam width about the
        y-axis."""

        self.assertEqual(self.beam.widthY_eta, 191.0)

    def test_edgeX_epsilon_eta(self):
        """`test_edgeX_epsilon_eta` tests the clip-level edge width about
        the x-axis."""

        self.assertEqual(self.beam.edgeX_epsilon_eta, 6.397368421052631)

    def test_edgeY_epsilon_eta(self):
        """`test_edgeY_epsilon_eta` tests the clip-level edge width about
        the y-axis."""

        self.assertEqual(self.beam.edgeY_epsilon_eta, 5.3519736842105265)

    def test_modPlateauUniformity_eta(self):
        """`ModPlateauUniformity_eta` tests the modified clip-level plateau
        uniformity."""

        self.assertEqual(self.beam.modPlateauUniformity_eta,
                         0.1643508206669702)

    def test_topHatFactor(self):
        """`test_topHatFactor` tests the top-hat factor."""

        self.assertEqual(self.beam.topHatFactor, 0.9014911235339008)


if __name__ == '__main__':
    unittest.main()
