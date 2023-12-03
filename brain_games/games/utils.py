from random import randint


def get_random_number(start, end):
    return randint(start, end)


def question(*args):
    return print('Question: ', *args)


def wrong_answer(correct, answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
