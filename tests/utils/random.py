import random
import string


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def random_boolean() -> bool:
    return bool(random.getrandbits(1))


def random_int() -> int:
    return random.randint(1, 9999)
