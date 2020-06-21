from collections import namedtuple
import random
import string

Bit = namedtuple('Bit', ['name', 'version'])


bits = [
    # Bit('dummy', '1.0')
]


def add_bit(bit):
    if bit not in bits:
        bits.append(bit)


def random_bit():
    return random.choice(bits)


def __random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def non_existing_bit():
    pass


def invalid_version_bit():
    pass
