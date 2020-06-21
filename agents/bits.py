import os
from collections import namedtuple
import random
import string

from bit_developer_agent import BIT_DEVELOPERS_DIRECTORY

Bit = namedtuple('Bit', ['name', 'version'])


def __bits_under_development():
    return next(os.walk(BIT_DEVELOPERS_DIRECTORY))[1]


def random_bit():
    return random.choice(__bits_under_development())


def __random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def non_existing_bit():
    pass


def invalid_version_bit():
    pass
