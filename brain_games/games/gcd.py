from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question():
    begin, end = 0, 100
    first, second = randint(begin, end), randint(begin, end)
    question = f'{first} {second}'
    correct_answer = gcd(first, second)
    return (question, str(correct_answer))
