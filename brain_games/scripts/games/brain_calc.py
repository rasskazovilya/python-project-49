#!/usr/bin/env python3
import random
from .. import printing


def play_calc_game():
    
    operations = ['+', '-', '*']

    for _ in range(3):
        operation = random.choice(operations)
        left_num = random.randint(1, 100)
        right_num = random.randint(1, 100)

        expression = '{} {} {}'.format(left_num, operation, right_num)

        printing.ask_question(expression)

        answer = input('Your answer: ')
        correct_answer = str(eval(expression))

        if not printing.is_answer_correct(answer, correct_answer):
            return False

    return True


def main():
    printing.main(play_calc_game)


if __name__ == '__main__':
    main()