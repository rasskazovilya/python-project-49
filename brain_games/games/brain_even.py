#!/usr/bin/env python3
import random
from brain_games.scripts import logic


def is_even(num):
    return num % 2 == 0


def even_game():
    rand_num = random.randint(1, 1000)
    correct_answer = 'yes' if is_even(rand_num) else 'no'

    return rand_num, correct_answer


def main():
    game_condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    logic.engine(even_game, game_condition)


if __name__ == '__main__':
    main()
