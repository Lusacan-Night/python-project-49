from operator import add, mul, sub
from random import choice
from brain_games.games.utils import question, get_random_number


def pick_random_operator():
    return choice(['*', '+', '-'])


def calculate_game():
    start = 0
    end = 100
    first = get_random_number(start, end)
    second = get_random_number(start, end)
    op = pick_random_operator()
    question(first, op, second)

    match op:
        case '*':
            return str(mul(first, second))
        case '+':
            return str(add(first, second))
        case '-':
            return str(sub(first, second))
