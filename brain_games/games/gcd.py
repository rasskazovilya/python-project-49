import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 1000


def gcd(num1, num2):
    '''Naive gcd calculation'''
    gcd_result = 1

    for i in range(1, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd_result = i

    return gcd_result


def play():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)

    expression = '{} {}'.format(num1, num2)
    correct_answer = str(gcd(num1, num2))

    return expression, correct_answer
