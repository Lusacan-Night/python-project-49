from .cli import welcome_user
from brain_games.games.games import game_loop


def main():
    name = welcome_user()
    print('Wha is the result of the expression?')
    game_loop(name, 'calc')


if __name__ == '__main__':
    main()
