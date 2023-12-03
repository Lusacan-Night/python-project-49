from math import gcd
from brain_games.games.utils import get_random_number


def gcd_game():
    start = 0
    end = 100
    first = get_random_number(start, end)
    second = get_random_number(start, end)
    print(f'Question: {first} {second}')
    return str(gcd(first, second))
