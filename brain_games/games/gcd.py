from math import gcd
from random import randint


def get_description():
    return 'Find the greatest common divisor of given numbers.'


def get_question():
    begin, end = 0, 100
    first = randint(begin, end)
    second = randint(begin, end)
    return f'{first} {second}'


def get_correct_answer(numbers):
    first, second = numbers.split(' ')
    first, second = int(first), int(second)
    return gcd(first, second)
