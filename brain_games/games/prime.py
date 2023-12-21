from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_BOUND = 1
UPPER_BOUND = 200
STEP = -1
RANGE_END = 1


def get_question_and_answer():
    question = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def is_prime(number):
    if number == 1:
        return False

    for i in range(number - 1, RANGE_END, STEP):
        if number % i == 0:
            return False
    return True
