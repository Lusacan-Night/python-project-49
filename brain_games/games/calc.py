from operator import add, mul, sub
from random import choice, randint


def calculate_game():
    start, end = 0, 100
    first = randint(start, end)
    second = randint(start, end)
    op = get_random_operator()
    return (first, op, second)


def calculate_right_answer(first, op, second):
    match op:
        case '*':
            return str(mul(first, second))
        case '+':
            return str(add(first, second))
        case '-':
            return str(sub(first, second))


def get_random_operator():
    return choice(['*', '+', '-'])
