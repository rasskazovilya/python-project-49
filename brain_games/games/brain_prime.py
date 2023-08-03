#!/usr/bin/env python3
import random
from brain_games.scripts import logic


def is_prime(num):
    '''Naive implementation of primality test'''
    if num == 1:
        return False

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def prime_game():
    rand_num = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(rand_num) else 'no'

    return rand_num, correct_answer


def main():
    game_condition = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    logic.engine(prime_game, game_condition)


if __name__ == '__main__':
    main()
