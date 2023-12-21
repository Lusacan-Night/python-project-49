from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_question_and_answer():
    first = randint(LOWER_BOUND, UPPER_BOUND)
    second = randint(LOWER_BOUND, UPPER_BOUND)
    question = f'{first} {second}'
    correct_answer = gcd(first, second)
    return (question, str(correct_answer))
