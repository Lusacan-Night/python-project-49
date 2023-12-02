import operator
import prompt

from random import randint, choice


def gen_random_number(begin, end):
    return randint(begin, end)


def even_game():
    question_number = gen_random_number(0, 100)
    print(f'Question: {question_number}')
    return is_even(question_number)


def calculate():
    first_num = gen_random_number(0, 100)
    second_num = gen_random_number(0, 100)
    op = pick_random_operator()
    print(f'{first_num} {op} {second_num}')

    match op:
        case '*':
            return str(operator.mul(first_num, second_num))
        case '+':
            return str(operator.add(first_num, second_num))
        case '-':
            return str(operator.sub(first_num, second_num))


def game_loop(name, game):
    for i in range(0, 3):
        if game == 'even':
            correct_answer = even_game()

        if game == 'calc':
            correct_answer = calculate()

        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def pick_random_operator():
    return choice(['*', '+', '-'])
