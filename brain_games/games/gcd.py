from math import gcd
from random import randint


def gcd_game():
    start, end = 0, 100
    first = randint(start, end)
    second = randint(start, end)
    return (first, second)


def calculate_gcd(first, second):
    return str(gcd(first, second))
