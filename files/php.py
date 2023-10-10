import logging

try:
    print("string" + 1)
except TypeError as e:
    logging.warning(f'{e}')
