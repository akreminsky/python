import random
import string

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


def encounter_dict(arr):
    enc_dict = {}
    for i in arr:
        if enc_dict.get(i) is None:
            enc_dict[i] = 1
            continue
        enc_dict[i] += 1
    return enc_dict


print(list_gen())
print(encounter_dict(list_gen()))
