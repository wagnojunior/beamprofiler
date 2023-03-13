"""
`BeamProfiler` is a Python package for laser beam analysis and
characterization according to ISO 13694, ISO 11145, and other non-ISO
definitions commonly used in the industry.
"""


__author__ = """Wagno Alves Braganca Junior"""
__email__ = 'wagnojunior@gmail.com'
__version__ = '1.2.0'


from beamprofiler import iso, niso, utils
from beamprofiler.beam import Beam

__all__ = ['Beam', 'iso', 'niso', 'utils']
