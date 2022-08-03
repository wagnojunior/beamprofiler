# -*- coding: utf-8 -*-
"""
This module defines the class `Beam`, which holds all the relevant data related
to the beam analysis.
"""

# =============================================================================
# Imports
# =============================================================================
import os

from beamprofiler.utils import data_processing as dp
from beamprofiler.iso import measured_quantities as mq
from beamprofiler.iso import characterizing_parameters as iso_cp
from beamprofiler.niso import characterizing_parameters as niso_cp


class Beam:
    """
    Class `Beam`.

    There are five categories of instance variables:
    1. defined by the user:
    2. defined in `utils.data_processing.py`
    3. defined in `iso.measured_quantities.py`
    4. defined in `iso.characterizing_parameters.py`
    5. defined in `niso.characterizing_parameters.py`
    """

    def __init__(self, path, fileName, eta, epsilon, mix):
        """
        Initialize an instance of type `Beam` with all relevant data related to
        the beam analysis.

        Parameters
        ----------
        path : str
            full path to the power density distribution file.
        fileName : str
            file name the power density distribution.
        eta : float
            upper clip level. 0 <= eta <= 1.
        epsilon : float
            lower clip level. 0 <= epsilon <= eta <= 1.
        mix : int
            number of normal mixtirues used in the normal fit. mix=[1, 2, 3].

        Returns
        -------
        None.
        """

        # =====================================================================
        # Instance variables defined by the user
        # =====================================================================
        self.eta = (
            eta
        )
        self.epsilon = (
            epsilon
        )
        self.mix = (
            mix
        )

        # =====================================================================
        # Instance variables define in utils.data_processing.py
        # =====================================================================
        self.raw_data = (
            dp.raw_data(os.path.join(path, fileName))
        )
        self.raw_header = (
            dp.raw_header(os.path.join(path, fileName))
        )
        self.raw_data_null = (
            dp.remove_background(self.raw_data,
                                 self.raw_header)
        )
        self.xResolution = (
            dp.get_xResolution(self.raw_header)
        )
        self.yResolution = (
            dp.get_yResolution(self.raw_header)
        )

        # =====================================================================
        # Instance variables defined in iso.measure_quantities.py
        # =====================================================================
        self.maxPowerDensity = (
            mq.max_power_density(self.raw_data_null)
        )
        self.totalPower = (
            mq.total_power(self.raw_data_null)
        )
        self.powerDensity_eta = (
            mq.clip_level_power_density(self.raw_data_null,
                                        self.eta)
        )
        self.power_eta = (
            mq.clip_level_power(self.raw_data_null,
                                self.eta)
        )

        # =====================================================================
        # Instance variables defined in iso.characterizing_parameters.py
        # =====================================================================
        self.fractionalPower_eta = (
            iso_cp.fractional_power(self.raw_data_null,
                                    self.eta)
        )
        self.centerX, self.centerY = (
            iso_cp.beam_center(self.raw_data_null.T,
                               self.raw_header)
        )
        self.widthX, self.widthY = (
            iso_cp.beam_width(self.raw_data_null.T,
                              self.raw_header,
                              self.centerX,
                              self.centerY)
        )
        self.aspectRatio = (
            iso_cp.beam_aspect_ratio(self.widthX,
                                     self.xResolution,
                                     self.widthY,
                                     self.yResolution)
        )
        self.irradiationArea_eta = (
            iso_cp.clip_level_irradiation_area(self.raw_data_null,
                                               self.eta)
        )
        self.irradiationArea_epsilon = (
            iso_cp.clip_level_irradiation_area(self.raw_data_null,
                                               self.epsilon)
        )
        self.averagePowerDensity_eta = (
            iso_cp.clip_level_average_power_density(self.power_eta,
                                                    self.irradiationArea_eta)
        )
        self.flatnessFactor_eta = (
            iso_cp.flatness_factor(self.averagePowerDensity_eta,
                                   self.maxPowerDensity)
        )
        self.beamUniformity_eta = (
            iso_cp.beam_uniformity(self.raw_data_null,
                                   self.raw_header,
                                   self.averagePowerDensity_eta,
                                   self.irradiationArea_eta,
                                   self.powerDensity_eta)
        )
        self.plateauUniformity_eta = (
            iso_cp.plateau_uniformity(self.raw_data_null,
                                      self.maxPowerDensity,
                                      self.mix)
        )
        self.edgeSteepness_eta = (
            iso_cp.edge_steepness(self.irradiationArea_epsilon,
                                  self.irradiationArea_eta)
        )

        # =====================================================================
        # Instance variables defined in niso.characterizing_parameters.py
        # =====================================================================
        self.widthX_eta = (
            niso_cp.clip_level_beam_width(self.raw_data_null.T,
                                          self.eta)
        )
        self.widthY_eta = (
            niso_cp.clip_level_beam_width(self.raw_data_null,
                                          self.eta)
        )
        self.edgeX_epsilon_eta = (
            niso_cp.clip_level_edge_width(self.raw_data_null.T,
                                          self.epsilon,
                                          self.eta)
        )
        self.edgeY_epsilon_eta = (
            niso_cp.clip_level_edge_width(self.raw_data_null,
                                          self.epsilon,
                                          self.eta)
        )
        self.modPlateauUniformity_eta = (
            niso_cp.plateau_uniformity(self.raw_data_null,
                                       self.mix)
        )
        self.topHatFactor = (
            niso_cp.top_hat_factor(dp.pre_top_hat(self.raw_data))
        )
