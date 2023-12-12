#!/usr/bin/env python3

import brain_games.games.calc as calc

from brain_games.games.engine import launch_game


def main():
    launch_game(calc.DESCRIPTION, calc.get_question)


if __name__ == '__main__':
    main()
