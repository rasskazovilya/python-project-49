import random


GAME_RULES = 'What number is missing in the progression?'
MIN_INITIAL = 1
MAX_INITIAL = 50
MAX_LAST = 200
MIN_TERMS = 5
MIN_DIFF = 3
MAX_DIFF = 10


def generate_progression(initial, last, diff):
    return list(map(str, range(initial, last, diff)))


def missing_number(progression, missing):
    index_missing = progression.index(missing)
    # note: replacing is inplace, so calling missing_number
    # multiple times will replace new number in existing sequence
    # every time
    progression[index_missing] = '..'
    return ' '.join(progression), missing


def play():
    initial = random.randint(MIN_INITIAL, MAX_INITIAL)
    last = random.randint(initial + MIN_TERMS * MAX_DIFF, MAX_LAST)
    diff = random.randint(MIN_DIFF, MAX_DIFF)

    progression = generate_progression(initial, last, diff)

    missing = random.choice(progression)
    progression, correct_answer = missing_number(progression, missing)
    return progression, correct_answer
