from random import choice
from brain_games.games.utils import get_random_number


def progression_game():
    start, end, step = get_random_number(1, 5), get_random_number(25, 50), get_random_number(1, 5)
    sequence = [str(x) for x in range(start, end, step)]
    random_num = choice(sequence)
    index_position = sequence.index(random_num)
    sequence[index_position] = '..'
    print(f'Question: {" ".join(sequence)}')
    return random_num
