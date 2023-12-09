from random import choice, randint


def get_description():
    return 'What is the result of the expression?'


def get_question():
    begin, end = 0, 100
    first, second = randint(begin, end), randint(begin, end)
    op = choice(['*', '+', '-'])
    return f'{first} {op} {second}'


def get_correct_answer(expression):
    first, op, second = expression.split(' ')
    first, second = int(first), int(second)
    match op:
        case '*':
            return f'{first * second}'
        case '+':
            return f'{first + second}'
        case '-':
            return f'{first - second}'
