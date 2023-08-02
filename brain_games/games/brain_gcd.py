#!/usr/bin/env python3
import random
from brain_games.scripts import logic


def gcd(num1, num2):
    '''Naive gcd calculation'''
    gcd_result = 1

    for i in range(1, min(num1, num2)+1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd_result = i

    return gcd_result


def gcd_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    expression = '{} {}'.format(num1, num2)
    correct_answer = str(gcd(num1, num2))

    return expression, correct_answer


def main():
    logic.engine(gcd_game)


if __name__ == '__main__':
    main()
