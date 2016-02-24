dicthash
========

dicthash is a small Python module that can generate md5 hashes from (arbitrarily nested) dictionaries. These dictionaries can contain arbitrary Python and NumPy data types. The goal of the module is to provide a hash function that can be safely used across different platforms. Its main use is to provide unique identifiers for parameter dictionaries used in parameter scans of neural network simulations.

It exposes just a single function to the user `dicthash.generate_hash_from_dict`.

Code status
===========

[![Build Status](https://travis-ci.org/INM-6/python-dicthash.svg?branch=master)](https://travis-ci.org/INM-6/python-dicthash)