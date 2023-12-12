#!/usr/bin/env python3

import brain_games.games.progression as progression

from brain_games.games.engine import launch_game


def main():
    launch_game(progression.DESCRIPTION, progression.get_question)


if __name__ == '__main__':
    main()
