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


* Free software: GNU General Public License v3
* Documentation: https://beamprofiler.readthedocs.io.


Features
--------

**BeamProfiler** imports the power density distribution of a laser beam and
generates a `.xlsx` report with the following items:


* *ISO 13694* [1]_: total power, clip-level power, maximum power density, clip-level
  power density, clip-level average power density, clip-level irradiation area,
  beam aspect ratio, fractional power, flatness factor, beam uniformity, plateau
  uniformity, edge steepness.
  
* *ISO 11145* [2]_: beam centroid, beam width.

|

.. figure:: images/iso.png
   :scale: 60 %
   :alt: Report of ISO parameters
 
   Report format of ISO parameters

|

* *Non-ISO*: clip-level beam width [3]_, clip-level edge width [3]_, modified
  plateau uniformity [4]_, top-hat factor [5]_.
  
|
  
.. figure:: images/non-iso.png
   :scale: 60 %
   :alt: Report of non-ISO parameters
 
   Report format of non-ISO parameters

|

* *Auxiliary graphs*: histogram, 2D heat map, 3D heat map, energy curve [5]_.

|

.. figure:: images/histogram.png
   :scale: 30 %
   :alt: Histogram
 
   Histogram

|   

.. figure:: images/2d_heat_map.png
   :scale: 30 %
   :alt: 2D heat map
 
   2D heat map
   
|
   
.. figure:: images/3d_heat_map.png
   :scale: 30 %
   :alt: 3D heat map
 
   3D heat map

|   
 
.. figure:: images/energy_curve.png
   :scale: 30 %
   :alt: Energy curve
 
   Energy curve

|  


.. [1] https://www.iso.org/standard/72945.html
.. [2] https://www.iso.org/standard/72944.html
.. [3] https://doi.org/10.1117/1.OE.60.6.060801
.. [4] https://doi.org/10.1117/12.611248
.. [5] https://doi.org/10.1117/12.143846




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
