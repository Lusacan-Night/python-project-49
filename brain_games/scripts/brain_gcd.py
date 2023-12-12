#!/usr/bin/env python3

import brain_games.games.gcd as gcd

from brain_games.games.engine import launch_game


def main():
    launch_game(gcd.DESCRIPTION, gcd.get_question)


if __name__ == '__main__':
    main()
