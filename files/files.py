import os
import random


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
