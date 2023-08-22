import random


GAME_CONDITION = 'What is the result of the expression?'


def game():
    operators = ['+', '-', '*']

    operator = random.choice(operators)
    left_num = random.randint(1, 100)
    right_num = random.randint(1, 100)

    expression = '{} {} {}'.format(left_num, operator, right_num)
    correct_answer = str(eval(expression))

    return expression, correct_answer
