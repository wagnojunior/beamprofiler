# -*- coding: utf-8 -*-
"""
Test file for a square beam.
"""
# =============================================================================
# Imports
# =============================================================================
import unittest
import pkg_resources

from beamprofiler import beam


class TestSquare(unittest.TestCase):
    """Tests for a perfectly flat-top beam."""

    def setUp(self):
        """`setUp` sets up the test fixtures."""

        path = pkg_resources.resource_filename(__name__,
                                               "fixtures")
        fileName = 'square_beam.xls'
        eta = 0.8
        epsilon = 0.1
        mix = 1
        self.beam = (
            beam.Beam(path, fileName, eta, epsilon, mix)
        )

    def test_totalPower(self):
        """`test_totalPower` tests the total power."""

        self.assertAlmostEqual(self.beam.totalPower, 10201000)

    def test_power_eta(self):
        """`test_power_eta` tests the clip-level power."""

        self.assertAlmostEqual(self.beam.power_eta, 10201000.0)

    def test_maxPowerDensity(self):
        """`test_maxPowerDensity` tests the maximum power density."""

        self.assertAlmostEqual(self.beam.maxPowerDensity, 1000)

    def test_powerDensity_eta(self):
        """`test_powerDensity_eta` tests the clip-level power density."""

        self.assertAlmostEqual(self.beam.powerDensity_eta, 800.0)

    def test_averagePowerDensity_eta(self):
        """`test_averagePowerDensity_eta` tests the clip-level average power
        density."""

        self.assertAlmostEqual(self.beam.averagePowerDensity_eta, 1000)

    def test_centerX(self):
        """`test_centerX` tests the center coordinate on the x-axis."""

        self.assertAlmostEqual(self.beam.centerX, 128)

    def test_centerY(self):
        """`test_centerY` tests the center coordinate on the y-axis."""

        self.assertAlmostEqual(self.beam.centerY, 128)

    def test_widthX(self):
        """`test_widthX` tests the beam width about the x-axis."""

        self.assertAlmostEqual(self.beam.widthX, 116.619)

    def test_widthY(self):
        """`test_widthY` tests the beam width about the y-axis."""

        self.assertAlmostEqual(self.beam.widthY, 116.619)

    def test_irradiationArea_epsilon(self):
        """`test_irradiationArea_epsilon` tests the lower clip-level
        irradiation area."""

        self.assertAlmostEqual(self.beam.irradiationArea_epsilon, 10201)

    def test_irradiationArea_eta(self):
        """`test_irradiationArea_eta` tests the upper clip-level irradiation
        area."""

        self.assertAlmostEqual(self.beam.irradiationArea_eta, 10201)

    def test_aspectRatio(self):
        """`test_aspectRatio` tests the beam aspect ratio."""

        self.assertAlmostEqual(self.beam.aspectRatio, 1.0)

    def test_fractionalPower_eta(self):
        """`test_fractionalPower_eta` tests the clip-level fractional power."""

        self.assertAlmostEqual(self.beam.fractionalPower_eta, 1.0)

    def test_flatnessFactor_eta(self):
        """`test_flatnessFactor_eta` tests the clip-level flatness factor."""

        self.assertAlmostEqual(self.beam.flatnessFactor_eta, 1.0)

    def test_beamUniformity_eta(self):
        """`test_beamUniformity_eta` tests the clip-level beam uniformity."""

        self.assertAlmostEqual(self.beam.beamUniformity_eta, 0.0)

    def test_plateauUniformity_eta(self):
        """`test_plateauUniformity_eta` tests the clip-level plateau
        uniformity."""

        self.assertAlmostEqual(self.beam.plateauUniformity_eta, 0.0)

    def test_edgeSteepness_eta(self):
        """`test_edgeSteepness_eta` tests the clip-level edge steepness."""

        self.assertAlmostEqual(self.beam.edgeSteepness_eta, 0.0)

    def test_widthX_eta(self):
        """`test_widthX_eta` tests the clip-level beam width about the
        x-axis."""

        self.assertAlmostEqual(self.beam.widthX_eta, 101.0)

    def test_widthY_eta(self):
        """`test_widthY_eta` tests the clip-level beam width about the
        y-axis."""

        self.assertAlmostEqual(self.beam.widthY_eta, 101.0)

    def test_edgeX_epsilon_eta(self):
        """`test_edgeX_epsilon_eta` tests the clip-level edge width about
        the x-axis."""

        self.assertAlmostEqual(self.beam.edgeX_epsilon_eta, 0.0)

    def test_edgeY_epsilon_eta(self):
        """`test_edgeY_epsilon_eta` tests the clip-level edge width about
        the y-axis."""

        self.assertAlmostEqual(self.beam.edgeY_epsilon_eta, 0.0)

    def test_modPlateauUniformity_eta(self):
        """`ModPlateauUniformity_eta` tests the modified clip-level plateau
        uniformity."""

        self.assertAlmostEqual(self.beam.modPlateauUniformity_eta, 0.0)

    def test_topHatFactor(self):
        """`test_topHatFactor` tests the top-hat factor."""

        self.assertAlmostEqual(self.beam.topHatFactor, 1.0)


if __name__ == '__main__':
    unittest.main()
