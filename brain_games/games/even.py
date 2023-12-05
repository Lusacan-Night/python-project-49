from random import randint


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_game():
    start, end = 1, 100
    return randint(start, end)
