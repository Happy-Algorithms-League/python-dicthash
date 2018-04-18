.. python-dicthash documentation master file, created by
   sphinx-quickstart on Thu Jan 18 11:20:08 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-dicthash's documentation!
===========================================

Generate portable md5 hashes from (arbitrarily nested)
dictionaries. These dictionaries can contain arbitrary Python and
NumPy data types. The goal of the module is to provide a hash function
that can be safely used across different platforms. Its main use is to
generate unique identifiers for parameter dictionaries used in
parameter scans of neural network simulations.

It exposes a single function to the user: `generate_hash_from_dict`.
The user can set two global parameters:

- `FLOAT_FACTOR`
  
  To ensure consistency between different systems, the library
  multiplies floats with the `FLOAT_FACTOR` and then converts them to
  integers.

- `FLOOR_SMALL_FLOATS`
  
  If the float is smaller than the inverse of the `FLOAT_FACTOR`, it
  cannot be safely converted. If `FLOOR_SMALL_FLOATS` is set to True,
  the library will round the float to zero. If set to False, it will
  throw an error in this case.
  
API reference
================
.. toctree::

   api_reference


Release Notes
=============
.. toctree::
   :maxdepth: 1

   release_notes

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
