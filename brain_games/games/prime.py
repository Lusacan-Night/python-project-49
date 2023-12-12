from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    begin, end = 1, 200
    question = randint(begin, end)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return (question, correct_answer)


def is_prime(number):
    step = -1
    range_end = 1

    if number == 1:
        return False

    for i in range(number - 1, range_end, step):
        if number % i == 0:
            return False
    return True
