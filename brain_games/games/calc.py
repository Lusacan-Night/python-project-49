from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def get_question():
    begin, end = 0, 100
    first, second = randint(begin, end), randint(begin, end)
    op = choice(['*', '+', '-'])

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
