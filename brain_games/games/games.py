import operator
import prompt

from brain_games.scripts.cli import welcome_user
from brain_games.games.utils import question, wrong_answer

from .gcd import gcd_game
from .even import even_game
from .calc import calculate_game
from .prime import prime_game
from .progression import progression_game


def game_loop(game):
    name = welcome_user()
    TRIES_COUNT = 3
    for i in range(TRIES_COUNT):
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
