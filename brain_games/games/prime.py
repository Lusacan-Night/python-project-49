from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    BEGIN, END = 1, 200
    question = randint(BEGIN, END)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def is_prime(number):
    STEP = -1
    RANGE_END = 1

    if number == 1:
        return False

    for i in range(number - 1, RANGE_END, STEP):
        if number % i == 0:
            return False
    return True
