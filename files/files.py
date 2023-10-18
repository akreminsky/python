import os
import random


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


def sum_files_six_nums(one: str, two: str):
    sum_var = 0
    try:
        with open(one, "r") as file:
            lines = sum(1 for line in file if line.rstrip())
        with open(one, "r") as file:
            if lines == 3:
                for s in file:
                    sum_var += int(s.rstrip())
            else:
                return f'File {one} contains more or less than 3 lines with integers to add'
        with open(two, "r") as file:
            lines_2 = sum(1 for line in file if line.rstrip())
        with open(two, "r") as file:
            if lines_2 == 3:
                for s in file:
                    sum_var += int(s.rstrip())
            else:
                return f'File {two} contains more or less than 3 lines with integers to add'
        return sum_var
    except TypeError as e:
        return f'{e}'
    except ValueError as e:
        return f'{e}'
    except FileNotFoundError as e:
        return f'{e}'


# files_creator()
print(sum_files_six_nums(f'{random.randint(1, 10)}.txt', f'{random.randint(1, 10)}.txt'))
print(sum_files_six_nums('1.txt', '2.txt'))


def type_maker(file_name):
    with open(file_name) as file:
        for i in file:
            args = i.split(" ")
            _ = Type(args[0], args[1], args[2])
