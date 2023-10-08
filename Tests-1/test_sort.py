import unittest
from random import randint

from sort_arr import sort_arr


class SortTests(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(sort_arr([0, 1, 2, 3, 0, 1, 2, 0]), [0, 0, 0, 1, 1, 2, 2, 3])

    def test_random(self):
        for i in range(100000):
            x = randint(-25, +25)
            y = randint(-25, +25)
            j = randint(-25, +25)
            p = randint(-25, +25)
            rand_array = [x, y, j, p]
            rand_array_sorted = sort_arr(rand_array)

            for j in range(len(rand_array_sorted)):
                if j < len(rand_array_sorted) - 1:
                    self.assertTrue(rand_array_sorted[j] <= rand_array_sorted[j + 1])

    def test_massive(self):
        test_list = sort_arr([i * -1 for i in range(3000)])
        for i in range(len(test_list)):
            if i < len(test_list) - 1:
                self.assertTrue(test_list[i] <= test_list[i + 1])

    def test_null(self):
        test_1 = []
        test_2 = [0 for _ in range(100)]
        self.assertEqual(test_1, sort_arr(test_1))
        self.assertEqual(test_2, sort_arr(test_2))


if __name__ == '__main__':
    unittest.main()
