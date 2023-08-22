import random


GAME_CONDITION = 'What number is missing in the progression?'


def generate_progression():
    MAX_START = 50
    MAX_END = 200
    MIN_PROGRESSION_ELEMENTS = 5
    MAX_STEP = 10

    start = random.randint(1, MAX_START)
    end = random.randint(
        start + MIN_PROGRESSION_ELEMENTS * MAX_STEP, MAX_END
    )
    step = random.randint(3, MAX_STEP)
    return list(map(str, range(start, end, step)))


def missing_number(progression):
    missing = random.choice(progression)
    index_missing = progression.index(missing)
    # note: replacing is inplace, so calling missing_number
    # multiple times will replace new number in existing sequence
    # every time
    progression[index_missing] = '..'
    return ' '.join(progression), missing


def game():
    progression = generate_progression()
    progression, correct_answer = missing_number(progression)
    return progression, correct_answer
