#!/usr/bin/env python3
import random
from brain_games.scripts import logic


def generate_progression():
    start = random.randint(1, 50)
    end = random.randint(start + 50, 200)
    step = random.randint(3, 10)
    return list(map(str, range(start, end, step)))


def missing_number(progression):
    missing = random.choice(progression)
    index_missing = progression.index(missing)
    # note: replacing is inplace, so calling missing_number
    # multiple times will replace new number in existing sequence
    # every time
    progression[index_missing] = '..'
    return ' '.join(progression), missing


def progression_game():
    progression = generate_progression()
    progression, correct_answer = missing_number(progression)
    return progression, correct_answer


def main():
    game_condition = 'What number is missing in the progression?'
    logic.engine(progression_game, game_condition)


if __name__ == '__main__':
    main()
