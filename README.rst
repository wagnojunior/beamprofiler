============
BeamProfiler
============


.. image:: https://img.shields.io/pypi/v/beamprofiler.svg
        :target: https://pypi.python.org/pypi/beamprofiler

.. image:: https://img.shields.io/travis/wagnojunior/beamprofiler.svg
        :target: https://travis-ci.com/wagnojunior/beamprofiler

.. image:: https://readthedocs.org/projects/beamprofiler/badge/?version=latest
        :target: https://beamprofiler.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


**BeamProfiler** is a Python package for laser beam analysis and characterization
according to ISO 13694, ISO 11145, and other non-ISO definitions commonly used
in the industry.

If you are new to the field of laser beam analysis or want to study it further
check out the :doc:`theory` for a list of reference papers and standards. For
more information on how to install **BeamProfiler**, go to the
:doc:`installation` page. If you need examples of how to use **BeamProfiler**
refer to the :doc:`usage` page.


* Free software: GNU General Public License v3
* Documentation: https://beamprofiler.readthedocs.io.


Features
--------

**BeamProfiler** imports the power density distribution of a laser beam and
generates a `.xlsx` report with the following items:


ISO parameters:
    total power, clip-level power, maximum power density, clip-level
    power density, clip-level average power density, clip-level irradiation
    area, beam aspect ratio, fractional power, flatness factor, beam
    uniformity, plateau uniformity, edge steepness, beam centroid, beam width.


Non-ISO parameters:
    clip-level beam width, clip-level edge width, modified plateau uniformity,
    top-hat factor.
  
Auxiliary graphs
    histogram, 2D heat map, 3D heat map, normalized energy curve.
    

Below are some illustrations:

.. figure:: images/iso.png
   :scale: 60 %
   :alt: Report of ISO parameters
 
   Report format of ISO parameters  

.. figure:: images/non-iso.png
   :scale: 60 %
   :alt: Report of non-ISO parameters
 
   Report format of non-ISO parameters


.. figure:: images/histogram.png
   :scale: 30 %
   :alt: Histogram
 
   Histogram  

.. figure:: images/2d_heat_map.png
   :scale: 30 %
   :alt: 2D heat map
 
   2D heat map
   
.. figure:: images/3d_heat_map.png
   :scale: 30 %
   :alt: 3D heat map
 
   3D heat map  
 
.. figure:: images/energy_curve.png
   :scale: 30 %
   :alt: Energy curve
 
   Energy curve


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
