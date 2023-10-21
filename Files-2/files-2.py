import os
from typing import List


def find_all_files_by_ext(dir: str, ext: str, flag: bool) -> List[str]:
    result = []
    for item in os.listdir(dir):
        if os.path.isfile(item):
            _, file_ext = os.path.splitext(os.path.join(dir, item))
            if file_ext == ext:
                result.append(item)
    if flag:
        sub_dirs = find_all_dirs(dir, False)
        for dir_sub in sub_dirs:
            for sub_item in os.listdir(os.path.join(dir, dir_sub)):
                if os.path.isfile(os.path.join(dir, dir_sub, sub_item)):
                    _, file_ext = os.path.splitext(os.path.join(dir, dir_sub, sub_item))
                    if file_ext == ext:
                        result.append(sub_item)
    return result


def find_all_dirs(dir: str, flag: bool) -> List[str]:
    result = []
    for item in os.listdir(dir):
        if os.path.isdir(item):
            result.append(item)
    if flag:
        subresult = list(result)
        for dir_sub in subresult:
            for sub_item in os.listdir(os.path.join(dir, dir_sub)):
                if os.path.isdir(os.path.join(dir, dir_sub, sub_item)):
                    result.append(sub_item)
    return result


def return_dirs_and_files(dir: str, ext: str, flag: bool) -> List[List[str]]:
    return [find_all_files_by_ext(dir, ext, flag), find_all_dirs(dir, flag)]


def delete_content(dir: str) -> int:
    if not return_dirs_and_files(dir, "", False)[1]:
        for item in os.listdir(dir):
            os.remove(item)
        return 1
    return 0


print(return_dirs_and_files(os.getcwd(), '.py', False))
print(return_dirs_and_files(os.getcwd(), '.py', True))
