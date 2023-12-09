from random import randint


def get_description():
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    begin, end = 1, 100
    return randint(begin, end)


def is_even(number):
    return number % 2 == 0


def get_correct_answer(number):
    return 'yes' if is_even(number) else 'no'
