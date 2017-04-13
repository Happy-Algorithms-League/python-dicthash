dicthash
========

Conveniently generate portable md5 hashes from (arbitrarily nested) dictionaries. These dictionaries can contain arbitrary Python and NumPy data types. The goal of the module is to provide a hash function that can be safely used across different platforms. Its main use is to generate unique identifiers for parameter dictionaries used in parameter scans of neural network simulations.

It exposes just a single function to the user `dicthash.generate_hash_from_dict`.

![Python2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python3.5](https://img.shields.io/badge/python-3.5-blue.svg)

Code status
===========

[![Build Status](https://travis-ci.org/INM-6/python-dicthash.svg?branch=master)](https://travis-ci.org/INM-6/python-dicthash)
