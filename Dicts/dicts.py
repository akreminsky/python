import random
import string
from typing import List, Set

dicts = {}
arr = []


def create_dict(dicts):
    for i in range(100):
        x = random.randint(0, 100000)
        s = ''.join(random.choices(string.ascii_letters, k=10))
        dicts[x] = s
        arr.append(x)
    return dicts


def delete_dict(dict, arr_keys):
    for i in arr_keys:
        dict.pop(i)


def list_gen():
    return [random.randint(1, 10) for i in range(100)]


def encounter_dict(arr: List[int], min_count: int) -> Set[int]:
    enc_dict = {}
    arr_with_min_counts = []
    for i in arr:
        if enc_dict.get(i) is None:
            enc_dict[i] = 1
            continue
        enc_dict[i] += 1
        if enc_dict[i] >= min_count:
            arr_with_min_counts.append(i)
    return set(arr_with_min_counts)

print(list_gen())
print(encounter_dict(list_gen(), 10))

print(encounter_dict([0, 1, 2, 3, 0, 1, 2, 0], 2))
