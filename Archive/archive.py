import os
from glob import glob
from zipfile import ZipFile


def scan_add(name: str, ext: str) -> None:
    with ZipFile(name, 'w') as zip:
        for i in glob(os.path.join(os.getcwd(), f'*{ext}')):
            zip.write(i)


print(scan_add('arc', '.htg'))
