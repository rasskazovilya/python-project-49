import random


GAME_RULES = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 100


def play():
    operators = ['+', '-', '*']

    operator = random.choice(operators)
    left_num = random.randint(MIN_NUM, MAX_NUM)
    right_num = random.randint(MIN_NUM, MAX_NUM)

    expression = '{} {} {}'.format(left_num, operator, right_num)
    correct_answer = str(eval(expression))

    return expression, correct_answer
