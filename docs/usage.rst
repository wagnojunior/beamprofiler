=====
Usage
=====

Power Density Distribution
--------------------------

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

1. Modify the *pdd* so that it matches the standard layout
2. Modify the source code so that it reflects your *pdd* file layout. See the
   :doc:`installation` section to find out how to install **BeamProfiler** from
   the :ref:`source <installation:from sources>`.



Standard Use
------------
   
To use **BeamProfiler** in a project::

    import beamprofiler
    

Custom Use
----------

