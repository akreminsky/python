import os
from glob import glob

# print(os.getcwd()+"/test.py")

# print(os.path.exists(os.getcwd()))

if not os.path.exists('level1'):
    os.makedirs(os.path.join('level1', 'level2', 'level3'))


# print(os.listdir())

# print(glob(os.path.join('*.py')))


# for root, dirs, files in os.walk('.'):
#    print(root)
#    print(dirs)
#    print(files)

# print(os.listdir(os.path.join(os.getcwd(), next(os.walk(os.getcwd()))[1][1])))

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


# print(find_all_files_by_ext(os.getcwd(), '.txt', True))

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
        return result


print(find_all_dirs(os.getcwd(), True))
