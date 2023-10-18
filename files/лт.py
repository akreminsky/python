from files import sum_files_six_nums

with open("new_file.txt", 'wt') as file1:
    file1.write("3\n")
    file1.write("5\n")
    file1.write("9\n")
with open("new_file_1.txt", 'wt') as file2:
    file2.write("2\n")
    file2.write("6\n")
    file2.write("190\n")
print(sum_files_six_nums("new_file.txt", "new_file_1.txt"))
