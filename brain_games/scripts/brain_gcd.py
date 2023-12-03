#!/usr/bin/env python3

from .cli import welcome_user
from brain_games.games.games import game_loop


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_loop(name, 'gcd')


if __name__ == '__main__':
    main()
