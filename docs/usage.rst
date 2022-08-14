=====
Usage
=====

Before you use
--------------

To use **BeamProfiler** you must first measure the :term:`pdd` of the laser
beam you want to analyze, and save it as `.csv`, `.xls`, or `.xlsx` in a known
location. **BeamProfiler** expects the :term:`pdd` to comply with the standard
layout to function properly. Below is a description of the standard layout and
an example.

.. note::
   **BeamProfiler** follows the zero-based indexing.

Header
   The header is located in the first row of the :term:`pdd` file, and it
   defines important measurement parameters, which must be present in the
   specified locations.

:Pixels X: Number of pixels in the x-axis (R0C5)
:Pixels Y: Number of pixels in the y-axis (R0C8)
:Size of windows X: Measurement window size in the x-axis measured in
   millimeter (R0C11)
:Size of windows Y: Measurement window size in the y-axis measured in
   millimeter (R0C14)
:Null Point: Value corresponding to the dark-field of the measurement tool
   (R0C17)

Body
   The body is located from the second row of the :term:`pdd` file, and it
   defines the power density of each individual pixel measured in
   :term:`ADC`/px.

Example
   The following table is a truncated :term:`pdd` that complies with the
   standard layout. It has a total of 65,536 pixels (256 pixels in both x-
   and y-axis), a measurement window area of approximately 1230 mm\ :sup:`2`
   (35.072 mm in both x- and y-axis), and a null point of 149.063 ADC/px.

   .. csv-table:: Standard layout
      :file: files/example.csv
      :header-rows: 1
      :class: special

If your :term:`pdd` was measured with the *PRIMES LaserDiagnosticsSoftware
v2.98.81*, then don't worry as it already complies with the standard layout.
If your :term:`pdd` was measured with another software and does not comply with
the standard layout, you have two options:

1. Modify the :term:`pdd` so that it matches the standard layout.
2. Modify the source code so that it reflects your :term:`pdd` file layout. To access the source code the the :ref:`Installation <installation:from sources>` section.

|

How to use
----------


1. **Download the example pdd**
   
   :download:`Download <../resources/lab_beam.xls>` the example :term:`pdd` file
   ``lab_beam.xls`` and save it in a known directory. This :term:`pdd`
   corresponds to a real laser beam used in the *laser-assisted bonding process
   (LAB)*. For more information on the LAB process, please refer to the
   :ref:`Theoretical background <theory-ref-1>` section. For this example we
   will paste the :term:`pdd` in the
   ``C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd`` folder.

   .. important::
      The auxiliary graphs and the beam analysis report file will be saved in this location.


2. **Start coding**

   Open your favorite IDE, create a new ``.py`` file, and save it in a known
   location. For this example we will create a file named ``example.py`` and save it in the ``C:\Users\wagnojunior.ab\Desktop\Tutorial`` folder. In ``example.py`` import **BeamProfiler** and enter the path to the :term:`pdd` file and its name as follows:

   .. code-block:: python
      :lineno-start: 1
      :caption: example.py

      import beamprofiler

      # Enter the path to the pdd file and its name
      path = r'C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd'
      fileName = 'lab_beam.xls'

   
   We can now move on and set a few user-defined values.


3. **Set the user-defined values**

   As introduced in the :ref:`Theoretical background <theory:introduction>`
   section, there are three user-defined values that must be set in order to run
   **BeamProfiler**. For this example we will set ``eta = 0.8``, ``epsilon = 0.1``, and ``mix = 1`` in ``example.py`` as follows:

   .. code-block:: python
      :lineno-start: 7
      :caption: example.py

      # Set the user-defined values
      eta = 0.8
      epsilon = 0.2
      mix = 1

   
   With these simple settings we can now leverage the full capabilities of
   **BeamProfiler**.


4. **Run the laser beam characterization**

   To run the laser beam characterization enter the following lines to ``example.py`` and execute the code. The analysis happens when we initialize an instance of type ``Beam`` with the function ``beamprofiler.Beam()``.

   .. code-block:: python
      :lineno-start: 12
      :caption: example.py

      # Initialize an instance of type Beam
      myBeam = beamprofiler.Beam(path, fileName, eta, epsilon, mix)

   .. autofunction:: beamprofiler.Beam.__init__

   
   The variable ``myBeam`` is created and all the relevant data related to the beam analysis are saved in it, including the following:

   .. _usage-step-4-iso:

   ISO parameters:
      total power, clip-level power, maximum power density, clip-level
      power density, clip-level average power density, clip-level irradiation
      area, beam aspect ratio, fractional power, flatness factor, beam
      uniformity, plateau uniformity, edge steepness, beam centroid, beam width.

   .. _usage-step-4-noniso:

   Non-ISO parameters:
      clip-level beam width, clip-level edge width, modified plateau uniformity,
      top-hat factor.

   .. note::
      The auxiliary graphs are generated based on the data stored in the variable ``myBeam``.


5. **Generate the histogram plot**

   To generate the histogram plot add the following lines to ``example.py`` and run the code. The histogram plot is saved when the function ``beamprofiler.utils.plot.histogram()`` is called.

   .. code-block:: python
      :lineno-start: 15
      :caption: example.py

      # Generate the histogram plot 
      beamprofiler.utils.plot.histogram(path, fileName, myBeam)

   .. autofunction:: beamprofiler.utils.plot.histogram
      :noindex:

   .. important::
         If the ``kwargs`` are omitted the histogram is ploted using the default
         format. See step :ref:`6 <usage-step-6>` for how to customize it


   The file ``lab_beam - histogram.png`` is created and saved in the
   ``C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd`` directory. This is a good chance to check if the number of normal mixtures used in the normal fit (variable ``mix`` defined in line 10) is appropriate.

   .. figure:: images/example_histogram_1.png
      :scale: 40 %
      :alt: Default histogram plot for the pdd lab_beam.xls using mix=1

      Default histogram plot for the pdd lab_beam.xls using mix=1


   We see that a single Gaussian distribution is not sufficient to fit the data at hand, which results in an unreliable laser beam characterization. Therefore, go back to line 10, change it so that two Gaussian distributions are used instead, and run the code again.

   .. warning::
         An ill-fitting normal distribution can negatively affect the soundness of the beam analysis.

   .. code-block:: python
      :lineno-start: 7
      :caption: example.py
      :emphasize-lines: 4

      # Set the user-defined values
      eta = 0.8
      epsilon = 0.2
      mix = 2

   .. figure:: images/example_histogram_2.png
      :scale: 40 %
      :alt: Default histogram plot for the pdd lab_beam.xls using mix=2

      Default histogram plot for the pdd lab_beam.xls using mix=2

   
   That is much better, right? For a reliable laser beam characterization do make sure that the normal fit is appropriate.

   .. hint::
         Use the histogram plot to check whether the number of normal mixtures used in the normal fit is appropriate.


.. _usage-step-6:

6. **Customize the histogram plot**

   It is possible to customize the histogram plot by specifying the ``kwargs``
   values. Go back to line 16, add the following lines, and run the code.

   .. code-block:: python
      :lineno-start: 15
      :caption: example.py
      :emphasize-lines: 2-9

      # Generate the histogram plot
      kwargs = {
         'n_bins': 512,
         'zoom': 2.5,
         'x1': 1600,
         'x2': 2000,
         'y1': 0,
         'y2': 2500
      }
      beamprofiler.utils.plot.histogram(path, fileName, myBeam, **kwargs)

   .. figure:: images/example_histogram_3.png
      :scale: 40 %
      :alt: Customized histogram plot for the pdd lab_beam.xls using mix=2

      Customized histogram plot for the pdd lab_beam.xls using mix=2

   
   See the difference? The number of histogram bins ``n_bins`` was increased from ``256`` to ``512``, the ``zoom`` of the inset image was increased from ``2`` to ``2.5``, and the top delimiter ``y2`` of the inset image was decreased from ``5000`` to ``2500``. The bottom delimiter ``y1``, the left delimiter ``x1``, and the right delimiter ``x2`` were not changed.


7. **Generate the 2D heat map plot**

   To generate the 2D heat map plot add the following lines to ``example.py`` and run the code. The 2D heat map plot is saved when the function
   ``beamprofiler.utils.plot.heat_map_2d()`` is called.

   .. code-block:: python
      :lineno-start: 26

      # Generate the 2D heat map plot
      beamprofiler.utils.plot.heat_map_2d(path, fileName, myBeam)

   .. autofunction:: beamprofiler.utils.plot.heat_map_2d
      :noindex:

   
   The file ``lab_beam - 2d heat map.png`` is created and saved in the ``C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd`` directory. As with the histogram plot, if the ``kwargs`` are omitted the 2D heat map is plotted using the default format.

   .. figure:: images/example_2d_heatmap_1.png
      :scale: 40 %
      :alt: Default 2D heat map plot for the pdd lab_beam.xls

      Default 2D heat map plot for the pdd lab_beam.xls

   
   It is possible to customize the 2D heat map plot by specifying the ``kwargs`` values. Go back to line 27, add the following lines, and execute the code.

   .. code-block:: python
      :lineno-start: 26
      :emphasize-lines: 2-6

      # Generate the 2D heat map plot
      kwargs = {
         'z_lim': 2500,
         'cross_x': 20,
         'cross_y': 20
      }
      beamprofiler.utils.plot.heat_map_2d(path, fileName, myBeam, **kwargs)


   .. figure:: images/example_2d_heatmap_2.png
      :scale: 40 %
      :alt: Customized 2D heat map plot for the pdd lab_beam.xls

      Customized 2D heat map plot for the pdd lab_beam.xls


   See the difference? The intensity axis was set to ``2500``, and the cross-section point was set to ``20 mm`` on both x- and y-axis.  
      
   .. hint::
      Modify the default ``kwargs`` to see the 2D heat map cross-section in a location other than the beam center.


8. **Generate the 3D heat map plot**
   
   To generate the 3D heat map plot add the following lines to ``example.py`` and execute the code. The 3D heat map plot is saved when the function ``beamprofiler.utils.plot.heat_map_3d()`` is called.

   .. code-block:: python
      :lineno-start: 34

      # Generate the 3D heat map plot
      beamprofiler.utils.plot.heat_map_3d(path, fileName, myBeam)

   .. autofunction:: beamprofiler.utils.plot.heat_map_3d
      :noindex:


   The file ``lab_beam - 3d heat map.png`` is created and saved in the ``C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd`` directory. As with the 2D heat map plot, if the ``kwargs`` are omitted the 3D heat map is plotted using the default format.

   .. figure:: images/example_3d_heatmap_1.png
         :scale: 40 %
         :alt: Default 3D heat map plot for the pdd lab_beam.xls

         Default 3D heat map plot for the pdd lab_beam.xls


   It is possible to customize the 2D heat map plot by specifying the ``kwargs`` values. Go back to line 35, add the following lines, and execute the code.

   .. code-block:: python
      :lineno-start: 35
      :emphasize-lines: 2-6

      # Generate the 3D heat map plot
      kwargs = {
         'elev': 30,
         'azim': 45,
         'dist': 15
      }
      beamprofiler.utils.plot.heat_map_3d(path, fileName, myBeam, **kwargs)


   .. figure:: images/example_3d_heatmap_2.png
         :scale: 40 %
         :alt: Customized 3D heat map plot for the pdd lab_beam.xls

         Customized 3D heat map plot for the pdd lab_beam.xls

   See the difference? The elevation angle was set to ``30 deg``, the azimuthal angle was set to ``45 deg``, and the distance was set to ``15``.

   .. hint::
      Modify the default ``kwargs`` to see the 3D heat map from different angles.


9. **Generate the normalized energy curve plot**
    
   To generate the normalized energy curve plot add the following lines to ``example.py`` and execute the code. The normalized energy curve plot is saved when the function ``beamprofiler.utils.plot.norm_energy_curve()`` is called.

   .. code-block:: python
      :lineno-start: 42

      # Generate the normalized energy curve plot
      beamprofiler.utils.plot.norm_energy_curve(path, fileName, myBeam)

   .. autofunction:: beamprofiler.utils.plot.norm_energy_curve
      :noindex:


   The file ``lab_beam - energy curve.png`` is created and saved in the ``C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd`` directory. Unlike the other auxiliary graphs, there are no customization for the normalized energy curve plot.


   .. figure:: images/example_energy_curve.png
         :scale: 40 %
         :alt: Default normalized energy curve plot for the pdd lab_beam.xls

         Default normalized energy curve plot for the pdd lab_beam.xls


10. **Generate the report file**
    
    To generate the beam analysis report file add the following lines to ``example.py`` and execute the code. The report is saved when the function ``beamprofiler.utils.report.write()``

    .. code-block:: python
      :lineno-start: 46

      # Generate the normalized energy curve plot
      beamprofiler.utils.report.write(path, fileName, myBeam)

   .. autofunction:: beamprofiler.utils.report.write
      :noindex:


   The file ``Beam Analysis - lab_beam.xlsx`` is created and saved in the ``C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd`` directory. It includes all the :ref:`ISO <usage-step-4-iso>` and :ref:`non-ISO <usage-step-4-noniso>` characterizing parameters listed in step 4, and the auxiliary graphs from steps 5–9.

   .. figure:: images/example_report.png
         :scale: 40 %
         :alt: Beam analysis report for the pdd lab_beam.xls

         Beam analysis report for the pdd lab_beam.xls

11. **Review the final code and try it yourself**
    
    Most likely the default format of the auxiliary graphs will not be suitable for every :term:`pdd`, therefore it is important that you are familiar with the customization available in **BeamProfiler**. Review the final code and try it yourself!
    
   .. code-block:: python
      :lineno-start: 1

      import beamprofiler

      # Enter the path to the pdd file and its name
      path = r'C:\Users\wagnojunior.ab\Desktop\Tutorial\pdd'
      fileName = 'lab_beam.xls'

      # Set the user-defined values
      eta = 0.8
      epsilon = 0.2
      mix = 2

      # Initialize an instance of type Beam
      myBeam = beamprofiler.Beam(path, fileName, eta, epsilon, mix)

      # Generate the histogram plot
      kwargs = {
          'n_bins': 512,
          'zoom': 2.5,
          'x1': 1600,
          'x2': 2000,
          'y1': 0,
          'y2': 2500
      }
      beamprofiler.utils.plot.histogram(path, fileName, myBeam, **kwargs)

      # Generate the 2D heat map plot
      kwargs = {
          'z_lim': 2500,
          'cross_x': 20,
          'cross_y': 20
      }
      beamprofiler.utils.plot.heat_map_2d(path, fileName, myBeam, **kwargs)

      # Generate the 3D heat map plot
      kwargs = {
          'elev': 30,
          'azim': 45,
          'dist': 15
      }
      beamprofiler.utils.plot.heat_map_3d(path, fileName, myBeam, **kwargs)

      # Generate the normalized energy curve plot
      beamprofiler.utils.plot.norm_energy_curve(path, fileName, myBeam)

      # Generate the report file
      beamprofiler.utils.report.write(path, fileName, myBeam)
