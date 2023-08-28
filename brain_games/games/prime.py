import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def is_prime(num):
    '''Naive implementation of primality test'''
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def play():
    rand_num = random.randint(MIN_NUM, MAX_NUM)
    correct_answer = 'yes' if is_prime(rand_num) else 'no'

    return rand_num, correct_answer
