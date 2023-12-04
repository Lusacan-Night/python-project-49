from brain_games.games.utils import question, get_random_number


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_game():
    start, end = 1, 100
    random_number = get_random_number(start, end)
    question(random_number)
    return is_even(random_number)
