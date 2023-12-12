from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    begin, end = 1, 100
    random_num = randint(begin, end)
    correct_answer = 'yes' if is_even(random_num) else 'no'
    return (random_num, correct_answer)


def is_even(number):
    return number % 2 == 0
