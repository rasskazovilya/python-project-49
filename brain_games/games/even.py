import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 1000


def is_even(num):
    return num % 2 == 0


def play():
    rand_num = random.randint(MIN_NUM, MAX_NUM)
    correct_answer = 'yes' if is_even(rand_num) else 'no'

    return rand_num, correct_answer
