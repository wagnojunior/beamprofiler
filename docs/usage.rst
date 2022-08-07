=====
Usage
=====

Before you use
--------------

To use **BeamProfiler** you must first measure the *power density distribution
(pdd)* of the laser beam you want to analyse, and save it as `.csv`, `.xls`, or
`.xlsx` in a known location. **BeamProfiler** expects the *pdd* to comply with
the standard layout to function properly. Below is a description of the standard
layout and an example.

.. note::
    **BeamProfiler** follows the zero-based indexing.

Header
    The header is located in the first row of the *pdd* file, and it defines
    important measurement parameters, which must be present in the specified
    locations.
      
    :Pixels X: Number of pixels in the x-axis (R0C5)
    :Pixels Y: Number of pixels in the y-axis (R0C8)
    :Size of windows X: Measurement window size in the x-axis measured in
        millimeter (R0C11)
    :Size of windows Y: Measurement window size in the y-axis measured in
        millimeter (R0C14)
    :Null Point: Value corresponding to the dark-field of the measurement tool
        (R0C17)
    
Body
    The body is located from the second row of the *pdd* file, and it defines
    the power density of each individual pixel measured in analog-digital counts
    per pixel (ADC/px).
    
Example
    The following table is a truncated *pdd* that complies with the standard
    layout. It has a total of 65,536 pixels (256 pixels in both x- and y-axis),
    a measurement window area of approximately 1230 mm\ :sup:`2` (35.072 mm in
    both x- and y-axis), and a null point of 149.063 ADC/px.
       
    .. csv-table:: Standard layout
       :file: files/example.csv
       :header-rows: 1
       :class: special

If your *pdd* was measured with the *PRIMES LaserDiagnosticsSoftware v2.98.81*,
then don't worry as it already complies with the standard layout. If your *pdd*
was measured with another software and does not comply with the standard layout,
you have two options:

1. Modify the *pdd* so that it matches the standard layout.
2. Modify the source code so that it reflects your *pdd* file layout. See the
   :doc:`installation` section to find out how to install **BeamProfiler** from
   the :ref:`source <installation:from sources>`.



How to use
----------
   
To use **BeamProfiler** in a project::

    import beamprofiler
    
Then, initialize an instance of type `Beam` with ``beamprofiler.Beam()``

.. autofunction:: beamprofiler.Beam.__init__

::

    path = 'path/to/the/pdd/file'
    fileName = 'pdd.xls'
    eta = 0.8
    epsilon = 0.2
    mix = 2
    
    myBeam = beamprofiler.Beam(path, fileName, eta, epsilon, mix)
    
    
After that, generate the auxiliary plots that will be included in the final
report. The available plots are: histogram, 2D heat map, 3D heat map, and
normalized energy curve.

To generate the histogram plot use ``beamprofiler.utils.plot.histogram()``. This
is a good chance to confirm if the number of normal mixtures used
if the normal fit (argument ``mix`` defined in ``beamprofiler.Beam()``) is
appropriate. The histogram can be customized by changing the default ``kwargs``
values.

.. autofunction:: beamprofiler.utils.plot.histogram

::

    kwargs = {
    'n_bins': 256,
    'zoom': 2,
    'x1': 1600,
    'x2': 2000,
    'y1': 0,
    'y2': 5000
    }   
    beamprofiler.utils.plot.histogram(path, fileName, myBeam, **kwargs)


To generate the 2D heat map plot use ``beamprofiler.utils.plot.heat_map_2d()``.
The 2D heat map plot can be customized by changing the default ``kwargs``
values.

.. autofunction:: beamprofiler.utils.plot.heat_map_2d

::

    kwargs = {
    'z_lim': 2500,
    'cross_x': 15,
    'cross_y': 15
    }  
    beamprofiler.utils.plot.heat_map_2d(path, fileName, myBeam, **kwargs)


To generate the 3D heat map plot use ``beamprofiler.utils.plot.heat_map_3d()``.
The 2D heat map plot can be customized by changing the default ``kwargs``
values.

.. autofunction:: beamprofiler.utils.plot.heat_map_3d

::

    kwargs = {
        'elev': 30,
        'azim': 45,
        'dist': 15
    }
    beamprofiler.utils.plot.heat_map_3d(path, fileName, myBeam, **kwargs)


To generate the normalized energy curve heat map plot use
``beamprofiler.utils.plot.norm_energy_curve()``. There are no customizations for
the normalized energy curve plot.

.. autofunction:: beamprofiler.utils.plot.norm_energy_curve

::

    beamprofiler.utils.plot.norm_energy_curve(path, fileName, myBeam)


Lastly, generate the summary report with ``beamprofiler.utils.report.write()``.

::

    beamprofiler.utils.report.write(path, fileName, myBeam)
    

The final code follows:

::

    import beamprofiler

    # Initialize an instance of type Beam
    path = 'path/to/the/pdd/file'
    fileName = 'pdd.xls'
    eta = 0.8
    epsilon = 0.2
    mix = 2
    
    myBeam = beamprofiler.Beam(path, fileName, eta, epsilon, mix)
    
    # Generate the histogram plot
    kwargs = {
        'n_bins': 256,
        'zoom': 2,
        'x1': 1600,
        'x2': 2000,
        'y1': 0,
        'y2': 5000
    }
    beamprofiler.utils.plot.histogram(path, fileName, myBeam, **kwargs)
    
    # Generate the 2D heat map plot
    kwargs = {
        'z_lim': 2500,
        'cross_x': 15,
        'cross_y': 15
    }
    beamprofiler.utils.plot.heat_map_2d(path, fileName, myBeam, **kwargs)
    
    # Generate the 3D heat map plot
    kwargs = {
        'elev': 30,
        'azim': 45,
        'dist': 15
    }
    beamprofiler.utils.plot.heat_map_3d(path, fileName, myBeam, **kwargs)
    
    # Generate the normalized energy curve
    beamprofiler.utils.plot.norm_energy_curve(path, fileName, myBeam)
    
    # Generate the summary report
    beamprofiler.utils.report.write(path, fileName, myBeam)
