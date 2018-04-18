dicthash
========

Generate portable md5 hashes from (arbitrarily nested) dictionaries. These dictionaries can contain arbitrary Python and NumPy data types. The goal of the module is to provide a hash function that can be safely used across different platforms. Its main use is to generate unique identifiers for parameter dictionaries used in parameter scans of neural network simulations.

It exposes a single function to the user `dicthash.generate_hash_from_dict`.


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
  

![Python2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python3.6](https://img.shields.io/badge/python-3.6-blue.svg)

Code status
===========

[![Build Status](https://travis-ci.org/INM-6/python-dicthash.svg?branch=master)](https://travis-ci.org/INM-6/python-dicthash)
[![Coverage Status](https://coveralls.io/repos/github/INM-6/python-dicthash/badge.svg?branch=master)](https://coveralls.io/github/INM-6/python-dicthash?branch=master)
