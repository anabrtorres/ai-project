import random

def getRandomIndice(arr):
    if not arr:
        return None

    return random.randint(0, len(arr) - 1)