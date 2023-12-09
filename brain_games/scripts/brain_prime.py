#!/usr/bin/env python3

from brain_games.games.engine import launch_game

from brain_games.games.prime import get_correct_answer
from brain_games.games.prime import get_description, get_question


def main():
    launch_game(get_description, get_question, get_correct_answer)


if __name__ == '__main__':
    main()
