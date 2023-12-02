import operator
import prompt

from math import gcd
from random import randint, choice


def gen_random_number(begin, end):
    return randint(begin, end)


def even_game(question_number):
    print(f'Question: {question_number}')
    return is_even(question_number)


def calculate_game(first_num, second_num, random_operator):
    print(f'Question: {first_num} {random_operator} {second_num}')

    match random_operator:
        case '*':
            return str(operator.mul(first_num, second_num))
        case '+':
            return str(operator.add(first_num, second_num))
        case '-':
            return str(operator.sub(first_num, second_num))


def gcd_game(first_num, second_num):
    print(f'Question: {first_num} {second_num}')
    return str(gcd(first_num, second_num))


def progression():
    start = gen_random_number(1, 5)
    end = gen_random_number(25, 50)
    step = start
    sequence = [str(x) for x in range(start, end, step)]
    random_num = choice(sequence)
    index_position = sequence.index(random_num)
    sequence[index_position] = '..'
    print(f'Question: {" ".join(sequence)}')
    return random_num


def game_loop(name, game):
    for i in range(0, 3):
        match game:
            case 'even':
                correct_answer = even_game(gen_random_number(0, 100))
            case 'calc':
                first = gen_random_number(0, 100)
                second = gen_random_number(0, 100)
                op = pick_random_operator()
                correct_answer = calculate_game(first, second, op)
            case 'gcd':
                first = gen_random_number(0, 100)
                second = gen_random_number(0, 100)
                correct_answer = gcd_game(first, second)
            case 'progression':
                correct_answer = progression()

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
