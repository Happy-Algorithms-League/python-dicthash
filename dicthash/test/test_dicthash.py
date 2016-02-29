# -*- coding: utf-8 -*-
"""
Unit and integration tests for the dicthash.dicthash module

"""

import unittest
import numpy as np

from .. import dicthash

# check whether h5py_wrapper is available
try:
    import h5py_wrapper.wrapper as h5w
    h5py_wrapper_found = True
except ImportError:
    h5py_wrapper_found = False


class DictHashTest(unittest.TestCase):

    def test_dicthash_yields_consistent_result(self):
        """
        assures that hash does not change upon internal changes of the
        module. changes to this test need good reasons as they will
        (most likely) break all hashes obtained before.

        """
        d0 = {
            'a': 'asd',
            'b': 0.12,
            3: {
                'c': [[3, 4, 5], [7, 9, 0]],
                'z': {
                    'y': 32.14,
                },
            },
            'd': 367,
            'e': np.array([[1, 2, np.sqrt(2)], [4, 5]]),
            'f': (('x', 5), ('y', 0.1)),
            u'é': u'€',
            'g': [{'b': 5}, {'c': [1, 2, 3.1415]}],
        }
        expected_hash = 'e81c4863ed95dabb53f1decc7dada421'
        hash0 = dicthash.generate_hash_from_dict(d0)
        self.assertEqual(expected_hash, hash0)

    def test_fails_with_non_dict(self):
        self.assertRaises(AssertionError, dicthash.generate_hash_from_dict, 2)

    def test_same_value_for_same_dict(self):
        d0 = {
            'a': [1, 2, 3],
            'b': 'asd',
            'c': 1.2,
        }
        d1 = {
            'a': [1, 2, 3],
            'b': 'asd',
            'c': 1.2,
        }

        hash0 = dicthash.generate_hash_from_dict(d0)
        hash1 = dicthash.generate_hash_from_dict(d1)

        self.assertEqual(hash0, hash1)

    def test_different_value_for_different_dict(self):
        d0 = {
            'a': [1, 2, 3],
            'b': 'asd',
            'c': 1.2,
        }
        d1 = {
            'a': [1, 2, 5],
            'b': 'asd',
            'c': 1.2,
        }

        hash0 = dicthash.generate_hash_from_dict(d0)
        hash1 = dicthash.generate_hash_from_dict(d1)

        self.assertNotEqual(hash0, hash1)

    def test_nested_dictionary(self):
        d0 = {
            'a': {
                'a0': [1, 2, 3],
                'a1': 'asd',
                'a2': 1.2,
            },
            'b': {
                'a0': [1, 2, 3],
                'a1': 'asd',
                'a2': 1.2,
            }
        }

        dicthash.generate_hash_from_dict(d0)

    def test_proper_flattening_nested_dict_keys(self):
        d0 = {
            'a': {
                'a0': {
                    'a00': '',
                    'a01': '',
                },
                'a1': '',
            },
            'b': '',
        }
        expected_raw = u'aa0a00aa0a01aa1b'
        self.assertEqual(dicthash.generate_hash_from_dict(d0, raw=True), expected_raw)

    def test_lists_are_flattened(self):
        d0 = {
            'a': [1, 2, 3],
            'b': [[1, 'x'], [5, 'y', 0.1]],
            'c': [{'b': 5}, {'c': [1, 2, 3.1415]}],
        }
        raw0 = dicthash.generate_hash_from_dict(d0, raw=True)
        self.assertTrue('(' not in raw0)
        self.assertTrue('[' not in raw0)
        self.assertTrue('{' not in raw0)

    def test_nested_lists(self):
        d0 = {
            'a': [[1.45, 2, 3], [4, 5, 6]],
            'b': 'asd',
            'c': 1.2,
        }
        dicthash.generate_hash_from_dict(d0)

    def test_tuples_are_flattened(self):
        d0 = {
            'a': (1, 2, 3),
            'b': ((1, 'x'), (5, 'y', 0.1)),
            'c': ({'b': 5}, {'c': (1, 2, 3.1415)}),
        }
        raw0 = dicthash.generate_hash_from_dict(d0, raw=True)
        self.assertTrue('(' not in raw0)
        self.assertTrue('[' not in raw0)
        self.assertTrue('{' not in raw0)

    def test_nested_tuples(self):
        d0 = {
            'a': (1, 2, 3),
            'b': (('x', 2.52), ('y', 1.98)),
        }
        dicthash.generate_hash_from_dict(d0)

    def test_numpy_arrays_are_flattened(self):
        d0 = {
            'a': np.array([1, 2, 3]),
            'b': np.array([[1, 'x'], [5, 'y', 0.1]]),
            'c': np.array([{'b': 5}, {'c': np.array([1, 2, 3.1415])}]),
        }
        raw0 = dicthash.generate_hash_from_dict(d0, raw=True)
        self.assertTrue('(' not in raw0)
        self.assertTrue('[' not in raw0)
        self.assertTrue('{' not in raw0)

    def test_nested_numpy_arrays(self):
        d0 = {
            'a': np.array([[1, 2, 3.678], [4, 5, 6]]),
            'b': 'asd',
            'c': 1.2,
        }
        dicthash.generate_hash_from_dict(d0)

    def test_integer_keys(self):
        d0 = {
            0: [1, 2, 3],
            1: 'asd',
            2: 1.2,
        }
        dicthash.generate_hash_from_dict(d0)

    def test_blacklist(self):
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

        hash0 = dicthash.generate_hash_from_dict(d0, blacklist=['d'])
        hash1 = dicthash.generate_hash_from_dict(d1, blacklist=['e'])

        self.assertEqual(hash0, hash1)

        hash0 = dicthash.generate_hash_from_dict(d0, blacklist=['a'])
        hash1 = dicthash.generate_hash_from_dict(d1, blacklist=['e'])

        self.assertNotEqual(hash0, hash1)

    def test_whitelist(self):
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
        hash1 = dicthash.generate_hash_from_dict(d1, whitelist=['a', 'b', 'c'])

        self.assertEqual(hash0, hash1)

        hash0 = dicthash.generate_hash_from_dict(d0, whitelist=['a', 'b', 'd'])
        hash1 = dicthash.generate_hash_from_dict(d1, whitelist=['a', 'b', 'c'])

        self.assertNotEqual(hash0, hash1)

    def test_invalid_blackwhitelist_raises_error(self):
        d0 = {
            'a': 5,
        }
        self.assertRaises(KeyError, dicthash.generate_hash_from_dict, d0, {'blacklist': ['a']})
        self.assertRaises(KeyError, dicthash.generate_hash_from_dict, d0, {'whitelist': ['c']})

    def test_unicode_keys_and_values(self):
        d0 = {
            u'é': 'asd',
            'a': u'é€',
            'b': 0.1212,
            3: [6, 7, 9],
        }

        dicthash.generate_hash_from_dict(d0)

    def test_same_unicode_and_nonunicode_strings_lead_to_same_hash(self):
        d0 = {
            'a': 'asd',
            'b': 0.12,
        }
        d1 = {
            u'a': u'asd',
            u'b': 0.12,
        }

        hash0 = dicthash.generate_hash_from_dict(d0)
        hash1 = dicthash.generate_hash_from_dict(d1)

        self.assertEqual(hash0, hash1)

    def test_lists_array_tuples_are_equal(self):
        d0 = {
            'a': [1, 2, 3],
        }
        d1 = {
            'a': np.array([1, 2, 3]),
        }
        d2 = {
            'a': (1, 2, 3),
        }

        hash0 = dicthash.generate_hash_from_dict(d0)
        hash1 = dicthash.generate_hash_from_dict(d1)
        hash2 = dicthash.generate_hash_from_dict(d2)

        self.assertEqual(hash0, hash1)
        self.assertEqual(hash1, hash2)

    @unittest.skipUnless(h5py_wrapper_found, 'No h5py_wrapper found.')
    def test_store_and_rehash_h5py(self):
        d0 = {
            'a': 'asd',
            'b': 0.12,
            'c': [3, 4, 5],
            'd': np.array([[3, 4, 5], [3, 4, 5]]),
            'e': True
        }
        hash0 = dicthash.generate_hash_from_dict(d0)
        h5w.add_to_h5('store_and_rehash_h5py.h5', {'d0': d0}, 'w')
        d0 = h5w.load_h5('store_and_rehash_h5py.h5', 'd0')
        hash1 = dicthash.generate_hash_from_dict(d0)

        self.assertEqual(hash0, hash1)
