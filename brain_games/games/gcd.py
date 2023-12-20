from math import gcd
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    BEGIN, END = 0, 100
    first, second = randint(BEGIN, END), randint(BEGIN, END)
    question = f'{first} {second}'
    correct_answer = gcd(first, second)
    return (question, str(correct_answer))
