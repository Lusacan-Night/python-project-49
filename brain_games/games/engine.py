import prompt

from brain_games.games.cli import welcome_user

from brain_games.games.gcd import gcd_game, calculate_gcd
from brain_games.games.even import is_even, even_game
from brain_games.games.prime import prime_game, calculate_prime
from brain_games.games.calc import calculate_game, calculate_right_answer
from brain_games.games.progression import progression_game, crypt_sequence


def question(*args):
    print('Question:', *args)


def wrong_answer(correct, answer):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")


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


def launch_even_game():
    even = even_game()
    question(even)
    return is_even(even)


def launch_calc_game():
    first, second, op = calculate_game()
    question(first, op, second)
    return calculate_right_answer(first, op, second)


def launch_gcd_game():
    first, second = gcd_game()
    question(first, second)
    return calculate_gcd(first, second)


def launch_progression_game():
    crypted_progression, crypted_number = crypt_sequence(progression_game())
    question(' '.join(crypted_progression))
    return crypted_number


def launch_prime_game():
    prime = prime_game()
    question(prime)
    return calculate_prime(prime)


def match_game(game):
    match game:
        case 'even':
            return launch_even_game()

        case 'calc':
            return launch_calc_game()

        case 'gcd':
            return launch_gcd_game()

        case 'progression':
            return launch_progression_game()

        case 'prime':
            return launch_prime_game()


def game_loop(game):
    TRIES_COUNT = 3
    name = welcome_user()
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
