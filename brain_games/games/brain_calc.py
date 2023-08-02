#!/usr/bin/env python3
import random
from brain_games.scripts import printing


def calc_game():
    operators = ['+', '-', '*']

    operator = random.choice(operators)
    left_num = random.randint(1, 100)
    right_num = random.randint(1, 100)

    expression = '{} {} {}'.format(left_num, operator, right_num)
    correct_answer = str(eval(expression))

    return expression, correct_answer


def main():
    printing.engine(calc_game)


if __name__ == '__main__':
    main()