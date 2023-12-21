from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'
LOWER_BOUND = 0
UPPER_BOUND = 100
MATH_OPERATOR_SYMBOLS = ['*', '+', '-']


def get_question_and_answer():
    first = randint(LOWER_BOUND, UPPER_BOUND)
    second = randint(LOWER_BOUND, UPPER_BOUND)
    op = choice(MATH_OPERATOR_SYMBOLS)

    question = f'{first} {op} {second}'
    correct_answer = 0

    match op:
        case '*':
            correct_answer = first * second
        case '+':
            correct_answer = first + second
        case '-':
            correct_answer = first - second

    return (question, str(correct_answer))
