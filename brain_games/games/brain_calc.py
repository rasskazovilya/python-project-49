#!/usr/bin/env python3
import random
from brain_games import logic


def calc_game():
    operators = ['+', '-', '*']

    operator = random.choice(operators)
    left_num = random.randint(1, 100)
    right_num = random.randint(1, 100)

    expression = '{} {} {}'.format(left_num, operator, right_num)
    correct_answer = str(eval(expression))

    return expression, correct_answer


def main():
    game_condition = 'What is the result of the expression?'
    logic.engine(calc_game, game_condition)


if __name__ == '__main__':
    main()
