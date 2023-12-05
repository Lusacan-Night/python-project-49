from random import randint


def prime_game():
    start, end = 1, 200
    return randint(start, end)


def calculate_prime(number):
    step = -1
    range_end = 1

    if number == 1:
            return 'no'

    for i in range(number - 1, range_end, step):
        if number % i == 0:
            return 'no'
    return 'yes'
