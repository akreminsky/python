import os


def coper(dir, flag):
    for item in os.listdir(dir):
        if os.path.isfile(item):
            _, file_ext = os.path.splitext(os.path.join(dir, item))
            print(file_ext)


print(coper(os.getcwd(), True))
