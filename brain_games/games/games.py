import operator
import prompt

from math import gcd
from random import randint, choice


def gen_random_number(begin, end):
    return randint(begin, end)


def question(question):
    return print(f'Question: {question}')


def even_game():
    question_number = gen_random_number(0, 100)
    question(question_number)
    return is_even(question_number)


def calculate_game():
    first = gen_random_number(0, 100)
    second = gen_random_number(0, 100)
    op = pick_random_operator()
    print(f'Question: {first} {op} {second}')

    match op:
        case '*':
            return str(operator.mul(first, second))
        case '+':
            return str(operator.add(first, second))
        case '-':
            return str(operator.sub(first, second))


def gcd_game():
    first = gen_random_number(0, 100)
    second = gen_random_number(0, 100)
    print(f'Question: {first} {second}')
    return str(gcd(first, second))


def progression_game():
    start = gen_random_number(1, 5)
    end = gen_random_number(25, 50)
    step = gen_random_number(1, 5)
    sequence = [str(x) for x in range(start, end, step)]
    random_num = choice(sequence)
    index_position = sequence.index(random_num)
    sequence[index_position] = '..'
    print(f'Question: {" ".join(sequence)}')
    return random_num


def prime_game():
    random_num = gen_random_number(1, 200)
    print(f'Question: {random_num}')
    for i in range(random_num - 1, 2, -1):
        if random_num % i == 0:
            return 'no'
    return 'yes'


def game_loop(name, game):
    for i in range(0, 3):
        match game:
            case 'even':
                correct_answer = even_game()
            case 'calc':
                correct_answer = calculate_game()
            case 'gcd':
                correct_answer = gcd_game()
            case 'progression':
                correct_answer = progression_game()
            case 'prime':
                correct_answer = prime_game()

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
