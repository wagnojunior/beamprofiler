.. default-role:: math

======================
Theoretical background
======================

Introduction
------------

.. note::
    This section covers the very minimum concepts one should understand in
    order to run **BeamProfiler**. For more detailed information check out the
    :ref:`References <theory:references>`, in special reference
    :ref:`1 <theory-ref-1>`.

Several ISO and non-ISO characterizing parameters must be associated with a
user-defined value called *clip-level* (denoted by the greek letter :term:`eta` 
`\eta`). The *clip-level* defines a fraction of the characterizing parameter
associated with it, and it is mathematically defined as (`0 \leq \eta < 1`).
For instance, if the maximum power density (`E_{max}`) of a laser beam is
`1000 ADC/px`, then the clip-level power density `E_{\eta CL}` considering
`\eta = 0.8` is `800 ADC/px`.

Similarly, some ISO and non-ISO characterizing parameters must be associated
with two clip-levels, namely the *upper clip-level* (denoted by the Greek
letter :term:`eta` `\eta`) and the *lower clip-level* (denoted by the Greek
letter :term:`epsilon` `\epsilon`). The *upper clip-level* and the *lower
clip-level* are mathematically expressed as `0 \leq \epsilon < \eta < 1`. The
values of :term:`eta` and :term:`epsilon` largely depend on the quality 
requirements of  the process that uses the laser beam.

Lastly, a few ISO and non-ISO characterizing parameters depend on a normal
fit of the the histogram associated with the :term:`pdd` of the laser beam.
Often times a single Gaussian distribution does not provide a proper fit,
therefore **BeamProfiler** offers the option to use a mixture of up to three
Gaussian distributions. You can set the variable ``mix`` to define the number
of normal mixtures used in the normal fit.


References
----------

On this section you will find a list of relevant references that will get you
started on the theory of laser beam analysis and deepen your understanding on
the field.

.. _theory-ref-1:

1. **Characterization of laser beams: theory and application in laser-assisted bonding process**
    
    This tutorial paper offers a pedagogical introduction to the theory and
    application of laser beam analysis through the use of a minimum working
    example. It is ideal for newcomers to the field of laser beam
    characterization.
    
    :Authors: Braganca, Wagno Alves and Kim, KyungOe
    :Journal: Optical Engineering, 60(6), 060801 (2021)
    :Access: https://doi.org/10.1117/1.OE.60.6.060801
    :Parameters: clip-level beam width, clip-level edge width.
    

.. _ISO 13694:

2. **ISO 136944:2018**
    
    The official ISO document that specifies the test methods and parameters
    for the characterization of laser beam power density distribution. It is
    handy for those already familiar to the field of laser beam characterization.
    
    :Authors: ISO/TC 172/SC 9 Laser and electro-optical systems
    :Access: https://www.iso.org/standard/72945.html
    :Parameters: total power, clip-level power, maximum power density,
                 clip-level, power density, clip-level average power density,
                 clip-level irradiation area, beam aspect ratio,
                 fractional power, flatness factor, beam uniformity, plateau
                 uniformity, edge steepness.
    

.. _ISO 11145:

3. **ISO 11145:2018**

    The official ISO document that defines basic terms, symbols, and units of
    measurement for the field of laser technology. It is suitable for those
    already familiar to the field of laser beam characterization.
    
    :Authors: ISO/TC 172/SC 9 Laser and electro-optical systems
    :Access: https://www.iso.org/standard/72944.html
    :Parameters: beam centroid, beam width.
    

.. _Flat-top:

4. **Flat-top shaped laser beams: reliability of standard parameters**

    This paper proposes a slight modification to the ISO standards in order
    to improve its reliability. It is ideal for those who fully understand the
    ISO standards and recognize its limitation.
    
    :Authors: Chang, Chao and Cramer, Larry and Danielson, Don and Norby, James
    :Proceedings: XV International Symposium on Gas Flow, Chemical Lasers, and
                  High-Power Lasers
    :Access: https://doi.org/10.1117/12.611248
    :Parameters: modified plateau uniformity.
    

.. _Specifying:

5. **Specifying excimer beam uniformity**

    This paper defines the *top-hat factor*, a non-ISO definition that serves a
    a general indicator of beam quality with a single number. It is relevant for
    those already familiar with the ISO standards and want to explore other
    characterizing parameters commonly used in the industry.
    
    :Authors: Abele, Chris Christian and Bunis, Jenifer Lynn and Caudle,
              George F and Klauminzer, Gary K
    :Proceedings: Laser Energy Distribution Profiles: Measurement and
                  Applications
    :Access: https://doi.org/10.1117/12.143846
    :Parameters: top-hat factor
    
