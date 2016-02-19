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
    return int(x * FLOAT_FACTOR)


def _generate_string_from_list(l):
    """convert a list to a string, by extracting every value. takes care
    of proper handling of floats to avoid rounding errors.

    """
    raw = ''
    for value in l:
        if isinstance(value, float):
            raw += str(_save_convert_float_to_int(value))
        elif isinstance(value, (list, np.ndarray)):
            raw += _generate_string_from_list(value)
        else:
            raw += str(value)
    return raw


def _generate_string_from_dict(d, blacklist, whitelist, prefix=''):
    """convert a dictionary to a string, by extracting every key value
    pair. takes care of proper handling of floats, lists and nested
    dictionaries.

    """
    raw = ''
    keys = np.sort(d.keys())
    if blacklist is None:
        blacklist = []

    if whitelist is None:
        whitelist = keys

    for key in whitelist:
        if key not in blacklist:
            value = d[key]
            if isinstance(value, dict):
                raw += _generate_string_from_dict(value, blacklist=None, whitelist=None, prefix=prefix.join(str(key)))
            else:
                raw += prefix + str(key)
                if isinstance(value, float):
                    raw += str(_save_convert_float_to_int(value))
                elif isinstance(value, (list, np.ndarray)):
                    raw += _generate_string_from_list(value)
                else:
                    raw += str(value)
    return raw


def generate_hash_from_dict(d, blacklist=None, whitelist=None, raw=False):
    """generates an md5 hash from a dictionary. takes care of extracting
    lists and arrays properly and avoids rounding errors of
    floats. makes sure the keys are read in a unique order. a
    blacklist of keys can be passed, that contain keys which should
    not be used to generate the hash. if a whitelist is given, only
    keys appearing in the whitelist are used to generate the hash.

    """
    assert(isinstance(d, dict))
    if blacklist is not None:
        validate_blackwhitelist(d, blacklist)
    if whitelist is not None:
        validate_blackwhitelist(d, whitelist)

    if raw:
        return _generate_string_from_dict(d, blacklist, whitelist)
    else:
        return hashlib.md5(_generate_string_from_dict(d, blacklist, whitelist)).hexdigest()


def validate_blackwhitelist(d, l):
    """validates that all entries in black/whitelist l, appear in the
    dictionary d"""
    for key in l:
        if key not in d.keys():
            raise KeyError('Key "%s" not found in dictionary. Invalid black/whitelist.' % (key))
