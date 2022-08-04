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




BeamProfiler is a Python package for laser beam analysis and characterization
according to ISO 13694, ISO 11145, and other non-ISO definitions commonly used
in the industry.


* Free software: GNU General Public License v3
* Documentation: https://beamprofiler.readthedocs.io.


Features
--------

*BeamProfiler* imports the power density distribution of a laser beam and generates a `.xlsx` report with the following items:

* ISO parameters:
  
  * Total power [1]_
  * Clip-level power [1]_
  * Maximum power density [1]_
  * Clip-level power density [1]_
  * Clip-level average power density [1]_
  * Beam centroid [2]_
  * Beam width  [2]_
  * Clip-level irradiation area [1]_
  * Beam aspect ratio [1]_
  * Fractional power [1]_
  * Flatness factor [1]_
  * Beam uniformity [1]_
  * Plateau uniformity [1]_
  * Edge steepness [1]_


* Non-ISO parameters:

  * Clip-level beam width [3]_
  * Clip-level edge width [3]_
  * Modified plateau uniformity [4]_
  * Top-hat factor [5]_


* Auxiliary graphs

  * Histogram analysis
  * 2D heat map
  * 3D heat map
  * Energy curve

.. [1] `ISO 13694`_
.. [2] `ISO 11145`_
.. [3] https://doi.org/10.1117/1.OE.60.6.060801
.. [4] https://doi.org/10.1117/12.611248
.. [5] needs to be updated

.. _ISO 13694: https://www.iso.org/standard/72945.html
.. _ISO 11145: https://www.iso.org/standard/72944.html


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
