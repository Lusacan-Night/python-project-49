#!/usr/bin/env python3

from .cli import welcome_user
from brain_games.games.games import game_loop


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    game_loop(name, 'even')


if __name__ == '__main__':
    main()
