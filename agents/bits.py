import os
from collections import namedtuple
import random
import string

import cpm_project_editor


BIT_DEVELOPERS_DIRECTORY = 'bit_developers'
Bit = namedtuple('Bit', ['name', 'version'])


def __all_bit_names():
    return next(os.walk(BIT_DEVELOPERS_DIRECTORY))[1]


def random_bit():
    all_bits = __all_bit_names()
    if all_bits:
        bit_name = random.choice(all_bits)
        bit_version = cpm_project_editor.bit_version(f'{BIT_DEVELOPERS_DIRECTORY}/{bit_name}')
        return Bit(bit_name, bit_version)
    return Bit(__random_string(), '1.0')


def __random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def non_existing_bit():
    pass


def invalid_version_bit():
    pass
