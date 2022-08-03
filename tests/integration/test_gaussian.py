# -*- coding: utf-8 -*-
"""
Test file for a Gaussian beam.
"""
# =============================================================================
# Imports
# =============================================================================
import unittest
import pkg_resources

from src.beamprofiler import beam


class TestGaussian(unittest.TestCase):
    """Tests for a Gaussian beam."""

    def setUp(self):
        """`setUp` sets up the test fixtures."""

        path = pkg_resources.resource_filename(__name__,
                                               "fixtures")
        fileName = 'gaussian_beam.xls'
        eta = 0.8
        epsilon = 0.1
        mix = 1
        self.beam = (
            beam.Beam(path, fileName, eta, epsilon, mix)
        )

    def test_totalPower(self):
        """`test_totalPower` tests the total power."""

        self.assertEqual(self.beam.totalPower, 5309116)

    def test_power_eta(self):
        """`test_power_eta` tests the clip-level power."""

        self.assertEqual(self.beam.power_eta, 1058333.0)

    def test_maxPowerDensity(self):
        """`test_maxPowerDensity` tests the maximum power density."""

        self.assertEqual(self.beam.maxPowerDensity, 1000)

    def test_powerDensity_eta(self):
        """`test_powerDensity_eta` tests the clip-level power density."""

        self.assertEqual(self.beam.powerDensity_eta, 800.0)

    def test_averagePowerDensity_eta(self):
        """`test_averagePowerDensity_eta` tests the clip-level average power
        density."""

        self.assertEqual(self.beam.averagePowerDensity_eta, 898.4151103565365)

    def test_centerX(self):
        """`test_centerX` tests the center coordinate on the x-axis."""

        self.assertEqual(self.beam.centerX, 128)

    def test_centerY(self):
        """`test_centerY` tests the center coordinate on the y-axis."""

        self.assertEqual(self.beam.centerY, 128)

    def test_widthX(self):
        """`test_widthX` tests the beam width about the x-axis."""

        self.assertEqual(self.beam.widthX, 116.133)

    def test_widthY(self):
        """`test_widthY` tests the beam width about the y-axis."""

        self.assertEqual(self.beam.widthY, 116.133)

    def test_irradiationArea_epsilon(self):
        """`test_irradiationArea_epsilon` tests the lower clip-level
        irradiation area."""

        self.assertEqual(self.beam.irradiationArea_epsilon, 12186)

    def test_irradiationArea_eta(self):
        """`test_irradiationArea_eta` tests the upper clip-level irradiation
        area."""

        self.assertEqual(self.beam.irradiationArea_eta, 1178)

    def test_aspectRatio(self):
        """`test_aspectRatio` tests the beam aspect ratio."""

        self.assertEqual(self.beam.aspectRatio, 1.0)

    def test_fractionalPower_eta(self):
        """`test_fractionalPower_eta` tests the clip-level fractional power."""

        self.assertEqual(self.beam.fractionalPower_eta, 0.19934260242194746)

    def test_flatnessFactor_eta(self):
        """`test_flatnessFactor_eta` tests the clip-level flatness factor."""

        self.assertEqual(self.beam.flatnessFactor_eta, 0.8984151103565365)

    def test_beamUniformity_eta(self):
        """`test_beamUniformity_eta` tests the clip-level beam uniformity."""

        self.assertEqual(self.beam.beamUniformity_eta, 0.06410517648424062)

    def test_plateauUniformity_eta(self):
        """`test_plateauUniformity_eta` tests the clip-level plateau
        uniformity."""

        self.assertEqual(self.beam.plateauUniformity_eta, 0.338983898389841)

    def test_edgeSteepness_eta(self):
        """`test_edgeSteepness_eta` tests the clip-level edge steepness."""

        self.assertEqual(self.beam.edgeSteepness_eta, 0.9033316921056951)

    def test_widthX_eta(self):
        """`test_widthX_eta` tests the clip-level beam width about the
        x-axis."""

        self.assertEqual(self.beam.widthX_eta, 35.57692307692308)

    def test_widthY_eta(self):
        """`test_widthY_eta` tests the clip-level beam width about the
        y-axis."""

        self.assertEqual(self.beam.widthY_eta, 35.57692307692308)

    def test_edgeX_epsilon_eta(self):
        """`test_edgeX_epsilon_eta` tests the clip-level edge width about
        the x-axis."""

        self.assertEqual(self.beam.edgeX_epsilon_eta, 45.779661016949156)

    def test_edgeY_epsilon_eta(self):
        """`test_edgeY_epsilon_eta` tests the clip-level edge width about
        the y-axis."""

        self.assertEqual(self.beam.edgeY_epsilon_eta, 45.779661016949156)

    def test_modPlateauUniformity_eta(self):
        """`ModPlateauUniformity_eta` tests the modified clip-level plateau
        uniformity."""

        self.assertEqual(self.beam.modPlateauUniformity_eta,
                         0.4700457634170046)

    def test_topHatFactor(self):
        """`test_topHatFactor` tests the top-hat factor."""

        self.assertEqual(self.beam.topHatFactor, 0.5007914662278968)


if __name__ == '__main__':
    unittest.main()
