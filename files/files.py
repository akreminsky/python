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


def sum_files(one, two):
    sum_var = 0
    with open(f'{one}.txt') as file:
        for s in file:
            sum_var += int(s.rstrip())
    with open(f'{two}.txt') as file:
        for s in file:
            sum_var += int(s.rstrip())


files_creator()
sum_files(random.randint(1, 10), random.randint(1, 10))
sum_files(1, 2)


def type_maker(file_name):
    with open(file_name) as file:
        for i in file:
            args = i.split(" ")
            _ = Type(args[0], args[1], args[2])
# TODO  тесты и обработка ошибок
