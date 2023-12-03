from brain_games.games.utils import question, get_random_number


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    start = 1
    end = 100
    question_number = get_random_number(start, end)
    question(question_number)
    return is_even(question_number)