#!/usr/bin/env python3
import random
from brain_games.scripts import logic


def generate_progression():
    start = random.randint(1, 50)
    end = random.randint(start, 200)
    step = random.randint(1, 20)
    return list(map(str, range(start, end, step)))


def missing_number(progression):
    missing = random.choice(progression)
    index_missing = progression.index(missing)
    # note: replacing is inplace, so calling missing_number
    # multiple times will replace new number in existing sequence
    # every time
    progression[index_missing] = '..'
    return progression, missing


def progression_game():
    progression = generate_progression()
    progression, correct_answer = missing_number(progression)
    return progression, correct_answer


def main():
    logic.engine(progression_game)


if __name__ == '__main__':
    main()
