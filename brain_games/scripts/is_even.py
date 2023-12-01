import prompt

from random import randint


def description():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def gen_random_number(begin, end):
    return randint(begin, end)


def game_loop(name):
    for i in range(0, 3):
        random_number = gen_random_number(0, 100)
        correct_answer = is_even(random_number)
        print(f'Question: {random_number}')
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
