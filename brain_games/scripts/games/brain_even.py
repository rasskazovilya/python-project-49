import random
from .. import printing


def is_even(num):
    return num % 2 == 0


def play_even_game():

    for _ in range(3):
        rand_num = random.randint(1, 1000)
        printing.ask_question(rand_num)

        answer = input('Your answer: ')
        correct_answer = 'yes' if is_even(rand_num) else 'no'

        if not printing.is_answer_correct(answer, correct_answer):
            return False

    return True


if __name__ == '__main__':
    printing.main(play_even_game)
