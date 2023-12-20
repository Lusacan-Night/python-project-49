from random import choice, randint


DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer():
    BEGIN, END = 0, 100
    first, second = randint(BEGIN, END), randint(BEGIN, END)
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
