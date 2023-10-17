import unittest
from random import randint

from sort_arr import sort_arr


class SortTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sort_arr([0, 1, 2, 3, 0, 1, 2, 0]), [0, 0, 0, 1, 1, 2, 2, 3])

    def test_random(self):
        for _ in range(100000):
            x = randint(-25, +25)
            y = randint(-25, +25)
            j = randint(-25, +25)
            p = randint(-25, +25)
            self.assertEqual(sort_arr([x, y, j, p]), sorted([x, y, j, p]))

    def test_massive(self):
        test_array = [i * -1 for i in range(3000)]
        self.assertEqual(sort_arr(test_array), sorted(test_array))


    def test_null(self):
        test_1 = []
        test_2 = [0 for _ in range(100)]
        self.assertEqual(test_1, sort_arr(test_1))
        self.assertEqual(test_2, sort_arr(test_2))


if __name__ == '__main__':
    unittest.main()
