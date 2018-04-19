# encoding: utf8

"""
dicthash
========

Generate portable md5 hashes from (arbitrarily nested)
dictionaries. These dictionaries can contain arbitrary Python and
NumPy data types. The goal of the module is to provide a hash function
that can be safely used across different platforms. Its main use is to
generate unique identifiers for parameter dictionaries used in
parameter scans of neural network simulations.

It exposes a single function to the user `dicthash.generate_hash_from_dict`.

"""

from .dicthash import generate_hash_from_dict

__version__ = '0.0.1'
