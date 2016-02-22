# -*- coding: utf-8 -*-

"""
DictHash.hash
=============

A module implementing an md5 hash function for (nested) dictionaries.

Functions
---------

generate_hash_from_dict - generate an md5 hash from a (nested) dictionary

"""

import numpy as np
import hashlib

FLOAT_FACTOR = 1e15


def _save_convert_float_to_int(x):
    """convert a float x to and int. avoid rounding errors on different
    platforms by shifting the floating point behind the last relevant
    digit.

    """
    if x < 1. / FLOAT_FACTOR:
        raise ValueError('Float too small for save conversion to integer.')
    return int(x * FLOAT_FACTOR)


def _generate_string_from_list(l):
    """convert a list to a string, by extracting every value. takes care
    of proper handling of floats to avoid rounding errors.

    """
    raw = ''
    for value in l:
        if isinstance(value, float):
            raw += unicode(_save_convert_float_to_int(value))
        elif isinstance(value, (list, np.ndarray)):
            raw += _generate_string_from_list(value)
        else:
            raw += unicode(value)
    return raw


def _generate_string_from_dict(d, blacklist, whitelist, prefix=''):
    """convert a dictionary to a string, by extracting every key value
    pair. takes care of proper handling of floats, lists and nested
    dictionaries.

    """
    raw = ''
    if blacklist is None:
        blacklist = []

    if whitelist is None:
        whitelist = d.keys()

    for key in sorted(whitelist):
        if key not in blacklist:
            value = d[key]
            if isinstance(value, dict):
                raw += _generate_string_from_dict(value, blacklist=None, whitelist=None, prefix=prefix + unicode(key))
            else:
                raw += prefix + unicode(key)
                if isinstance(value, float):
                    raw += unicode(_save_convert_float_to_int(value))
                elif isinstance(value, (list, np.ndarray)):
                    raw += _generate_string_from_list(value)
                else:
                    raw += unicode(value)
    return raw


def generate_hash_from_dict(d, blacklist=None, whitelist=None, raw=False):
    """
    Generate an md5 hash from a (nested) dictionary.

    Takes care of extracting nested dictionaries, lists and arrays and
    avoids rounding errors of floats. Makes sure keys are read in a
    unique order. A blacklist of keys can be passed, that can contain
    keys which should be excluded from the hash. If a whitelist is
    given, only keys appearing in the whitelist are used to generate
    the hash. All strings are converted to unicode to generate the
    hash, i.e., the hash does not distinguish between strings provided
    in ascii or unicode format.

    Parameters
    ----------
    d : dictionary object
        Dictionary to compute the hash from.
    blacklist : list, optional
                List of keys which *are not* used for generating the hash.
    whitelist : list, optional
                List of keys which *are* used for generating the hash.
    raw : bool, optional
          if True, return the unhashed string.

    Returns
    -------
    : string
      The hash generated from the dictionary, or the unhashed string if
      raw is True.

    Example
    -------
    >>> import dicthash.dicthash as dhsh
    >>> d = {'a': 'asd', 'b': 0.12, 3: {'c': [3, 4, 5]}}
    >>> dhsh.generate_hash_from_dict(d)
    '6725c9cd61278978b124dbd61a1cfb6a'

    """
    assert(isinstance(d, dict)), 'Please provide a dictionary.'
    if blacklist is not None:
        validate_blackwhitelist(d, blacklist)
    if whitelist is not None:
        validate_blackwhitelist(d, whitelist)

    if raw:
        return _generate_string_from_dict(d, blacklist, whitelist).encode('utf-8')
    else:
        return hashlib.md5(_generate_string_from_dict(d, blacklist, whitelist).encode('utf-8')).hexdigest()


def validate_blackwhitelist(d, l):
    """validates that all entries in black/whitelist l, appear in the
    dictionary d"""
    for key in l:
        if key not in d.keys():
            raise KeyError('Key "%s" not found in dictionary. Invalid black/whitelist.' % (key))
