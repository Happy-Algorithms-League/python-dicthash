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
