import operator
import prompt

from brain_games.scripts.cli import welcome_user
from math import gcd
from random import randint, choice


def gen_random_number(start, end):
    return randint(start, end)


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def pick_random_operator():
    return choice(['*', '+', '-'])


def question(question):
    return print(f'Question: {question}')


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start = 1
    end = 100
    question_number = gen_random_number(start, end)
    question(question_number)
    return is_even(question_number)


def calculate_game():
    print('What is the result of the expression?')
    start = 0
    end = 100
    first = gen_random_number(start, end)
    second = gen_random_number(start, end)
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
    print('Find the greatest common divisor of given numbers.')
    start = 0
    end = 100
    first = gen_random_number(start, end)
    second = gen_random_number(start, end)
    print(f'Question: {first} {second}')
    return str(gcd(first, second))


def progression_game():
    print('What number is missing in the progression?')

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
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start = 1
    end = 200
    step = -1
    random_num = gen_random_number(start, end)
    print(f'Question: {random_num}')

    for i in range(random_num - 1, 1, step):
        if random_num % i == 0:
            return 'no'
    return 'yes'


def wrong_answer(correct, answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")


def game_loop(game):
    name = welcome_user()
    tries_count = 3
    for i in range(tries_count):
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
            wrong_answer(correct_answer, answer)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
