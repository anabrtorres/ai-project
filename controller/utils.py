import random


def get_random_indice_from_array(arr):
    """Return a random indice from array"""
    if not arr:
        return None

    return random.randint(0, len(arr) - 1)
