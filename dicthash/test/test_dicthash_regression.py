# -*- coding: utf-8 -*-
"""
Unit and integration tests for the dicthash.dicthash module

"""

import pytest

from .. import dicthash


def test_depth_matters_in_nested_dict():
    d0 = {
        'a': {
            'a0': 4,
            'a1': 5,
        },
        'b': 'asd',
    }
    d1 = {
        'a': {
            'a0': 4,
        },
        'a1': 5,
        'b': 'asd',
    }

    hash0 = dicthash.generate_hash_from_dict(d0)
    hash1 = dicthash.generate_hash_from_dict(d1)

    assert(hash0 != hash1)

def test_error_for_failing_float_conversion():
    d0 = {
        'a': 1e-15,
    }
    d1 = {
        'a': 1e-16,
    }

    d2 = {
        'a': -1e-15,
    }
    d3 = {
        'a': -1e-16,
    }

    dicthash.generate_hash_from_dict(d0)
    dicthash.generate_hash_from_dict(d2)
    with pytest.raises(ValueError):
        dicthash.generate_hash_from_dict(d1)
    with pytest.raises(ValueError):
        dicthash.generate_hash_from_dict(d3)

def test_shuffled_whitelist_leads_to_same_hash():
    d0 = {
        'a': [1, 2, 3],
        'b': 'asd',
        'c': 1.2,
        'd': 123,
    }
    d1 = {
        'a': [1, 2, 3],
        'b': 'asd',
        'c': 1.2,
        'e': 'xyz',
    }

    hash0 = dicthash.generate_hash_from_dict(d0, whitelist=['a', 'b', 'c'])
    hash1 = dicthash.generate_hash_from_dict(d1, whitelist=['b', 'c', 'a'])

    assert(hash0 == hash1)

def test_mixed_string_integer_keys():
    d0 = {
        'a': 'asd',
        'b': 0.12,
        3: {'c': [3, 4, 5]}
    }
    dicthash.generate_hash_from_dict(d0)

def test_unicode_is_not_replaced_or_ignored():
    d0 = {
        u'é': 'asd',
        'a': u'é€',
        'b': 0.1212,
        3: [6, 7, 9],
    }
    d1 = {
        u'€': 'asd',
        'a': u'€é',
        'b': 0.1212,
        3: [6, 7, 9],
    }

    hash0 = dicthash.generate_hash_from_dict(d0)
    hash1 = dicthash.generate_hash_from_dict(d1)

    assert(hash0 != hash1)

def test_storing_zero():
    d0 = {
        'a': 0,
        'b': 0.,
        'c': [0, 0.],
    }

    dicthash.generate_hash_from_dict(d0)

def test_storing_negative_number():
    d0 = {
        'a': -1,
        'b': -1.,
    }

    dicthash.generate_hash_from_dict(d0)
