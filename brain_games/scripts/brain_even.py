#!/usr/bin/env python3

import brain_games.games.even as even

from brain_games.engine import launch_game


def main():
    launch_game(even.DESCRIPTION, even.get_question_and_answer)


if __name__ == '__main__':
    main()
