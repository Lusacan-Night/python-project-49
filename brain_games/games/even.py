from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 100


def get_question_and_answer():
    random_num = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = 'yes' if is_even(random_num) else 'no'
    return (random_num, correct_answer)


def is_even(number):
    return number % 2 == 0
