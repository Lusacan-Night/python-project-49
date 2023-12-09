from random import randint


def get_description():
    return 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_question():
    begin, end = 1, 200
    return randint(begin, end)


def is_prime(number):
    step = -1
    range_end = 1

    if number == 1:
        return False

    for i in range(number - 1, range_end, step):
        if number % i == 0:
            return False
    return True


def get_correct_answer(number):
    return 'yes' if is_prime(number) else 'no'