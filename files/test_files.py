import unittest


class FilesTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sort_arr([0, 1, 2, 3, 0, 1, 2, 0]), [0, 0, 0, 1, 1, 2, 2, 3])
