# -*- coding: utf-8 -*-
"""
This module handles the report generation of the beam analysis.
"""

# =============================================================================
# Imports
# =============================================================================
import os
import xlsxwriter


def write(path, fileName, beam):
    """
    `write` writes the beam analysis report in a `.xlsx` format.

    Parameters
    ----------
    path : str
        directory where the input file is saved.
    fileName : str
        name of the input file.
    beam : Beam
        object of type `Beam`.

    Returns
    -------
    None.

    """

    # Name of the input and output file
    fileName = os.path.splitext(fileName)[0]
    outFile = 'Beam Analysis - ' + fileName + '.xlsx'

    # Create a new Excel file
    wb = xlsxwriter.Workbook(os.path.join(path, outFile))

    # Create formats for this workbook
    bold = wb.add_format({
        'bold': True
    })
    italic = wb.add_format({
        'italic': True
    })
    number = wb.add_format({
        'num_format': '#,##0.00'
    })

    # Define a method to write the header
    def header(sheet):

        sheet.write('A1', 'Item', bold)
        sheet.write('B1', 'Value', bold)
        sheet.write('C1', 'Unit', bold)
        sheet.write('D1', 'Remark', bold)

    # Define a method to write the sub header
    def sub_header(sheet, row, value):

        sheet.write('A'+str(row), value, italic)

    # Define a method to write an empty line
    def empty_line(sheet, row):

        sheet.write('A'+str(row), '')

    # Define a method to write the entry
    def entry(sheet, row, value):

        sheet.write('A'+str(row), value[0])
        sheet.write('B'+str(row), value[1], number)
        sheet.write('C'+str(row), value[2])
        sheet.write('D'+str(row), value[3])

    # Define a method to insert an image
    def image(sheet, cell, path):

        sheet.insert_image(cell, path)

    def column_width(sheet):

        sheet.set_column('A:A', 30)
        sheet.set_column('B:B', 15)
        sheet.set_column('D:D', 70)

    # =========================================================================
    # Create and populate the ISO sheet
    # =========================================================================
    ws = wb.add_worksheet('ISO')
    column_width(ws)

    header(ws)

    sub_header(ws, 2, 'Beam power')
    entry(ws, 3, ['Total power',
                  beam.totalPower,
                  'ADC',
                  'Independent of the clip-level'])
    entry(ws, 4, ['Clip-level power',
                  beam.power_eta,
                  'ADC',
                  'Clip-level: ' + str(beam.eta*100) + '%'])
    empty_line(ws, 5)

    sub_header(ws, 6, 'Beam power density')
    entry(ws, 7, ['Maximum power density',
                  beam.maxPowerDensity,
                  'ADC',
                  'Independent of the clip-level'])
    entry(ws, 8, ['Clip-level power density',
                  beam.powerDensity_eta,
                  'ADC',
                  'Clip-level: ' + str(beam.eta*100) + '%'])
    entry(ws, 9, ['Clip-level average power density',
                  beam.averagePowerDensity_eta,
                  'ADC',
                  'Clip-level: ' + str(beam.eta*100) + '%'])
    empty_line(ws, 10)

    sub_header(ws, 11, 'Beam position')
    entry(ws, 12, ['Beam centroid x-axis',
                   beam.centerX * beam.xResolution,
                   'mm',
                   'Independent of the clip-level'])
    entry(ws, 13, ['Beam centroid y-axis',
                   beam.centerY * beam.yResolution,
                   'mm',
                   'Independent of the clip-level'])
    empty_line(ws, 14)

    sub_header(ws, 15, 'Effective beam size')
    entry(ws, 16, ['Beam width x-axis',
                   beam.widthX * beam.xResolution,
                   'mm',
                   'Independent of the clip-level'])
    entry(ws, 17, ['Beam width y-axis',
                   beam.widthY * beam.yResolution,
                   'mm',
                   'Independent of the clip-level'])
    entry(ws, 18, ['Clip-level irradiation area',
                   beam.irradiationArea_epsilon,
                   'mm',
                   'Clip-level: ' + str(beam.epsilon*100) + '%'])
    entry(ws, 19, ['Clip-level irradiation area',
                   beam.irradiationArea_eta,
                   'mm',
                   'Clip-level: ' + str(beam.eta*100) + '%'])
    empty_line(ws, 20)

    sub_header(ws, 21, 'Beam shape')
    entry(ws, 22, ['Beam aspect ratio',
                   beam.aspectRatio,
                   'N/A',
                   'Independent of the clip-level. Equals 1 for a perfect '
                   'square'])
    entry(ws, 23, ['Fractional power',
                   beam.fractionalPower_eta,
                   'N/A',
                   'Clip-level: ' + str(beam.eta*100) + '%.'])
    entry(ws, 24, ['Flatness factor',
                   beam.flatnessFactor_eta,
                   'N/A',
                   'Clip-level: ' + str(beam.eta*100) + '%. Equals 1 for a '
                   'perfect flat top'])
    entry(ws, 25, ['Beam uniformity',
                   beam.beamUniformity_eta,
                   'N/A',
                   'Clip-level: ' + str(beam.eta*100) + '%. Equals 0 for a '
                   'perfect flat top with vertical edges'])
    entry(ws, 26, ['Plateau uniformity',
                   beam.plateauUniformity_eta,
                   'N/A',
                   'Clip-level: ' + str(beam.eta*100) + '%. Equals 0 for a '
                   'perfect flat top'])
    entry(ws, 27, ['Edge steepness',
                   beam.edgeSteepness_eta,
                   'N/A',
                   'Clip-level: ' + str(beam.eta*100) + '%. Equals 0 for a '
                   'perfect vertical edge'])

    image(ws, 'E1', os.path.join(path, fileName + ' - histogram.png'))
    image(ws, 'E17', os.path.join(path, fileName + ' - 2d heat map.png'))
    image(ws, 'J17', os.path.join(path, fileName + ' - 3d heat map.png'))

    # =========================================================================
    # Create and populate the non ISO sheet
    # =========================================================================
    ws = wb.add_worksheet('non ISO')
    column_width(ws)

    header(ws)

    sub_header(ws, 2, 'Effective beam size')
    entry(ws, 3, ['Clip-level beam width x-axis',
                  beam.widthX_eta * beam.xResolution,
                  'mm',
                  'Clip-level: ' + str(beam.eta*100) + '%'])
    entry(ws, 4, ['Clip-level beam width y-axis',
                  beam.widthY_eta * beam.yResolution,
                  'mm',
                  'Clip-level: ' + str(beam.eta*100) + '%'])
    entry(ws, 5, ['Clip-level edge width x-axis',
                  beam.edgeX_epsilon_eta * beam.xResolution,
                  'mm',
                  'Clip-level: ' + str(beam.epsilon*100) + '% and '
                  + str(beam.eta*100) + '%'])
    entry(ws, 6, ['Clip-level edge width y-axis',
                  beam.edgeY_epsilon_eta * beam.yResolution,
                  'mm',
                  'Clip-level: ' + str(beam.epsilon*100) + '% and '
                  + str(beam.eta*100) + '%'])
    empty_line(ws, 7)

    sub_header(ws, 8, 'Beam shape')
    entry(ws, 9, ['Plateau uniformity',
                  beam.modPlateauUniformity_eta,
                  'N/A',
                  'Clip-level: ' + str(beam.eta*100) + '%. Equals 0 for a '
                  'perfect flat top'])
    entry(ws, 10, ['Top-hat factor',
                   beam.topHatFactor,
                   'N/A',
                   'Independent of the clip-level. Equals 1 for a perfect '
                   'square'])

    image(ws, 'E1', os.path.join(path, fileName + ' - energy curve.png'))

    try:
        wb.close()
    except xlsxwriter.exceptions.FileCreateError:
        print("The file is currently open and won't be saved. Please, close "
              "the file and run the analysis again.")
