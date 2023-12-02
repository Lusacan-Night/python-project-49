from .cli import welcome_user
from brain_games.games.games import game_loop


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    game_loop(name, 'progression')


if __name__ == '__main__':
    main()
