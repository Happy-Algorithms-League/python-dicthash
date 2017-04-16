# -*- coding: utf-8 -*-

"""
DictHash.hash
=============

A module implementing an md5 hash function for (nested) dictionaries.

Functions
---------

generate_hash_from_dict - generate an md5 hash from a (nested) dictionary

"""

from future.builtins import str
import hashlib
FLOAT_FACTOR = 1e15

try:
    basestring  # attempt to evaluate basestring
except NameError:
    basestring = str

def _save_convert_float_to_int(x):
    """convert a float x to and int. avoid rounding errors on different
    platforms by shifting the floating point behind the last relevant
    digit.

    """
    if abs(x) > 0. and abs(x) < 1. / FLOAT_FACTOR:
        raise ValueError('Float too small for safe conversion to integer.')
    return int(x * FLOAT_FACTOR)


def _unpack_value(value, prefix=''):
        try:
            return _generate_string_from_dict(value, blacklist=None, whitelist=None, prefix=prefix)
        except AttributeError:
            # not a dict
            try:
                return prefix + _generate_string_from_iterable(value)
            except TypeError:
                # not an iterable
                if isinstance(value, float):
                    return prefix + str(_save_convert_float_to_int(value))
                else:
                    return prefix + str(value)


def _generate_string_from_iterable(l):
    """convert a list to a string, by extracting every value. takes care
    of proper handling of floats to avoid rounding errors.

    """
    # we need to handle strings separately to avoid infinite recursion
    # due to their iterable property
    if isinstance(l, basestring):
        return str(l)
    else:
        raw = [_unpack_value(value) for value in l]
        return ''.join(raw)


def _generate_string_from_dict(d, blacklist, whitelist, prefix=''):
    """convert a dictionary to a string, by extracting every key value
    pair. takes care of proper handling of floats, lists and nested
    dictionaries.

    """
    if whitelist is None:
        whitelist = d.keys()
    if blacklist is not None:
        whitelist = [key for key in whitelist if key not in blacklist]
    # Sort whitelist according to the keys converted to str
    raw = [_unpack_value(d[key], prefix + str(key)) for key in sorted(whitelist, key=str)]
    return ''.join(raw)


def generate_hash_from_dict(d, blacklist=None, whitelist=None, raw=False):
    """
    Generate an md5 hash from a (nested) dictionary.

    Takes care of extracting nested dictionaries, lists and arrays and
    avoids rounding errors of floats. Makes sure keys are read in a
    unique order. A blacklist of keys can be passed, that can contain
    keys which should be excluded from the hash. If a whitelist is
    given, only keys appearing in the whitelist are used to generate
    the hash. All strings are converted to unicode, i.e., the hash
    does not distinguish between strings provided in ascii or unicode
    format. Lists, np.ndarrays and tuples are treated equally, i.e., an
    array-like item [1,2,3], np.array([1,2,3]) or (1,2,3) will lead
    to the same hash if they are of the same type.

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
    if not isinstance(d, dict):
        raise TypeError('Please provide a dictionary.')

    if blacklist is not None:
        validate_blackwhitelist(d, blacklist)
    if whitelist is not None:
        validate_blackwhitelist(d, whitelist)
    raw_string = _generate_string_from_dict(d, blacklist, whitelist)
    if raw:
        return raw_string
    else:
        return hashlib.md5(raw_string.encode('utf-8')).hexdigest()


def validate_blackwhitelist(d, l):
    """validates that all entries in black/whitelist l, appear in the
    dictionary d"""
    for key in l:
        if key not in d:
            raise KeyError('Key "{key}" not found in dictionary. Invalid black/whitelist.'.format(key=key))
