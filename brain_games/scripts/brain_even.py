#!/usr/bin/env python3

from .cli import welcome_user
from .is_even import description, game_loop


def main():
    name = welcome_user()
    description()
    game_loop(name)


if __name__ == '__main__':
    main()
