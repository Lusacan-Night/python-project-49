#!/usr/bin/env python3

import brain_games.games.prime as prime

from brain_games.games.engine import launch_game


def main():
    launch_game(prime.DESCRIPTION, prime.get_question)


if __name__ == '__main__':
    main()
