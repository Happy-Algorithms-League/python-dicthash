.. python-dicthash documentation master file, created by
   sphinx-quickstart on Thu Jan 18 11:20:08 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-dicthash's documentation!
===========================================

Conveniently generate portable md5 hashes from (arbitrarily nested)
dictionaries. These dictionaries can contain arbitrary Python and
NumPy data types. The goal of the module is to provide a hash function
that can be safely used across different platforms. Its main use is to
generate unique identifiers for parameter dictionaries used in
parameter scans of neural network simulations.

It exposes just a single function to the user: `generate_hash_from_dict`.


API reference
================
.. toctree::

   api_reference


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
