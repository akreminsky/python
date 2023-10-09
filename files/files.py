import random


def files_creator():
    for i in range(10):
        with open(f'{i + 1}.txt', "wt") as file:
            for _ in range(3):
                file.write(f'{random.randint(0, 10)} \n')


files_creator()
