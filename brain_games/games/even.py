import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def game():
    rand_num = random.randint(1, 1000)
    correct_answer = 'yes' if is_even(rand_num) else 'no'

    return rand_num, correct_answer
