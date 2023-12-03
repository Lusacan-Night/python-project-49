import prompt

from brain_games.scripts.cli import welcome_user
from brain_games.games.utils import wrong_answer

from .gcd import gcd_game
from brain_games.games.even import even_game
from brain_games.games.calc import calculate_game
from .prime import prime_game
from .progression import progression_game


def games_description(game):
    description = {
        'gcd':
            'Find the greatest common divisor of given numbers.',
        'even':
            'Answer "yes" if the number is even, otherwise answer "no".',
        'calc':
            'What is the result of the expression?',
        'prime':
            'Answer "yes" if given number is prime. Otherwise answer "no".',
        'progression':
            'What number is missing in the progression?'
    }
    return description.get(game)


def match_game(game):
    match game:
        case 'even':
            return even_game()
        case 'calc':
            return calculate_game()
        case 'gcd':
            return gcd_game()
        case 'progression':
            return progression_game()
        case 'prime':
            return prime_game()


def game_loop(game):
    name = welcome_user()
    TRIES_COUNT = 3
    print(games_description(game))
    for i in range(TRIES_COUNT):
        correct_answer = match_game(game)
        answer = prompt.string('Your answer: ')

        if correct_answer == answer:
            print('Correct!')
        else:
            wrong_answer(correct_answer, answer)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
