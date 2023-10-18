import os
import random
from typing import List


class Type:
    def __init__(self, work, age, height):
        self.__work = work
        self.__age = age
        self.__height = height


def files_creator():
    for i in range(10):
        if f'{i + 1}.txt' in os.listdir():
            with open(f'{i + 1}.txt', "wt") as file:
                for _ in range(3):
                    file.write(f'{random.randint(0, 10)} \n')


def sum_files_six_nums(one: str, two: str) -> List[str]:
    sum_var = 0
    files_to_add = [one, two]

    for file_added in files_to_add:
        try:
            with open(file_added, "r") as file:
                lines = sum(1 for line in file if line.rstrip())
            with open(file_added, "r") as file:
                if lines == 3:
                    for s in file:
                        sum_var += int(s.rstrip())
                else:
                    return [0, f'File {file_added} contains more or less than 3 lines with integers to add']
        except TypeError as e:
            return ['0', f'Error in file{file_added}:{e}']
        except ValueError as e:
            return ['0', f'Error in file{file_added}:{e}']
        except FileNotFoundError as e:
            return ['0', f'Error in file{file_added}:{e}']
    return [str(sum_var), "Ok"]


files_creator()
# print(sum_files_six_nums(f'{random.randint(1, 10)}.txt', f'{random.randint(1, 10)}.txt'))
print(type(sum_files_six_nums('1.txt', '2.txt')[0]))


def type_maker(file_name):
    with open(file_name) as file:
        for i in file:
            args = i.split(" ")
            _ = Type(args[0], args[1], args[2])
