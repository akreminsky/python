from random import randint

for i in range(100000):
    x = randint(-25, +25)
    y = randint(-25, +25)
    j = randint(-25, +25)
    p = randint(-25, +25)
    rand_array = [x, y, j, p]
    # rand_array_sorted = sort_arr(rand_array)

    rand_array.sort()
    print(rand_array)
