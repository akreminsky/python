import unittest

from dicts import encounter_dict


class SortTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(encounter_dict([0, 1, 2, 3, 0, 1, 2, 0]), {0: 3, 1: 2, 2: 2, 3: 1})
