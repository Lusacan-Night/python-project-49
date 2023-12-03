from brain_games.games.utils import question, get_random_number

def prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    start = 1
    end = 200
    step = -1
    random_num = get_random_number(start, end)
    question(random_num)

    for i in range(random_num - 1, 1, step):
        if random_num % i == 0:
            return 'no'
    return 'yes'
