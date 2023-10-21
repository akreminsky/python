import unittest

from files import sum_files_six_nums


class FilesTests(unittest.TestCase):

    def test_regression(self):
        with open("new_file.txt", 'wt') as file1:
            file1.write("3\n")
            file1.write("5\n")
            file1.write("9\n")
        with open("new_file_1.txt", 'wt') as file2:
            file2.write("2\n")
            file2.write("6\n")
            file2.write("190\n")
        self.assertTrue(sum_files_six_nums("new_file.txt", "new_file_1.txt")[0] == 215)

    def test_empty_file(self):
        with open("new_file.txt", 'wt') as file1:
            file1.write("3\n")
            file1.write("8\n")
            file1.write("9\n")
        with open("new_file_1.txt", 'wt') as file2:
            file2.write("\n")
        self.assertTrue(sum_files_six_nums("new_file.txt",
                                           "new_file_1.txt")[
                            1] == 1)

    def test_string_line(self):
        with open("new_file.txt", 'wt') as file1:
            file1.write("3\n")
            file1.write("stringstring\n")
            file1.write("9\n")
        with open("new_file_1.txt", 'wt') as file2:
            file2.write("3\n")
            file2.write("2\n")
            file2.write("9\n")
        self.assertTrue(sum_files_six_nums("new_file.txt", "new_file_1.txt")[1] == 3)
