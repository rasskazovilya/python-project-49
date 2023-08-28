import random


GAME_RULES = 'What number is missing in the progression?'
MAX_INITIAL = 1
MAX_INITIAL = 50
MAX_LAST = 200
MIN_TERMS = 5
MIN_DIFF = 3
MAX_DIFF = 10


def generate_progression(
    min_init, max_init, min_diff, max_diff, max_last, min_terms
):
    initial = random.randint(min_init, max_init)
    last = random.randint(initial + min_terms * max_diff, max_last)
    diff = random.randint(min_diff, max_diff)
    return list(map(str, range(initial, last, diff)))


def missing_number(progression, missing):
    index_missing = progression.index(missing)
    # note: replacing is inplace, so calling missing_number
    # multiple times will replace new number in existing sequence
    # every time
    progression[index_missing] = '..'
    return ' '.join(progression), missing


def play():
    progression = generate_progression(
        MAX_INITIAL, MAX_INITIAL, MIN_DIFF, MAX_DIFF, MAX_LAST, MIN_TERMS
    )
    missing = random.choice(progression)
    progression, correct_answer = missing_number(progression, missing)
    return progression, correct_answer
