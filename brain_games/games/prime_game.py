import random


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    '''Naive implementation of primality test'''
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def game():
    rand_num = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(rand_num) else 'no'

    return rand_num, correct_answer
