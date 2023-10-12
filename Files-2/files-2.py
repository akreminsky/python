import os
from glob import glob


def find_all_files_by_ext(dir, ext, flag):
    files = []
    if not flag:
        for i in glob(os.path.join(dir, f'*{ext}')):
            files.append(os.path.basename(i))
        return files
    for _, dirs, _ in os.walk(dir):
        for subdir in dirs:
            subresult = glob(os.path.join(os.getcwd(), subdir, f'*{ext}'))
            if len(subresult) > 0:
                for i in subresult:
                    files.append(os.path.basename(i))
        if len(glob(os.path.join(f'*{ext}'))) > 0:
            for j in glob(os.path.join(f'*{ext}')):
                files.append(j)
        break
    return files


def find_all_dirs(dir, flag):
    for _, dirs, _ in os.walk(dir):
        result = []
        if flag:
            for subdir in dirs:
                result.append(subdir)
                for _, dirs_level, _ in os.walk(subdir):
                    for i in dirs_level:
                        result.append(i)
                    break
            return result
        return dirs


def return_dirs_and_files(dir, ext, flag):
    return [find_all_files_by_ext(dir, ext, flag), find_all_dirs(dir, flag)]


print(return_dirs_and_files(os.getcwd(), '.py', True))
