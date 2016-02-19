# -*- coding: utf-8 -*-
"""
Unit and integration tests for the dicthash.dicthash module

"""

import unittest

from .. import dicthash


class DictHashRegressionTest(unittest.TestCase):

    def test_depth_matters_in_nested_dict(self):
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

        self.assertNotEqual(hash0, hash1)

    def test_error_for_failing_float_conversion(self):
        d0 = {
            'a': 1e-15,
        }
        d1 = {
            'a': 1e-16,
        }

        dicthash.generate_hash_from_dict(d0)
        self.assertRaises(ValueError, dicthash.generate_hash_from_dict, d1)

    def test_shuffled_whitelist_leads_to_same_hash(self):
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

        self.assertEqual(hash0, hash1)

    def test_mixed_string_integer_keys(self):
        d0 = {
            'a': 'asd',
            'b': 0.12,
            3: {'c': [3, 4, 5]}
        }
        dicthash.generate_hash_from_dict(d0)
