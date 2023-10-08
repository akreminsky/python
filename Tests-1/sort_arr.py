import sys

sys.setrecursionlimit(10000)


def sort_arr(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        more = [i for i in array[1:] if i > pivot]
        return sort_arr(less) + [pivot] + sort_arr(more)
