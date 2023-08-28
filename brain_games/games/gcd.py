import random


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    '''Naive gcd calculation'''
    gcd_result = 1

    for i in range(1, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            gcd_result = i

    return gcd_result


def game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    expression = '{} {}'.format(num1, num2)
    correct_answer = str(gcd(num1, num2))

    return expression, correct_answer
