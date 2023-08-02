import random
from scripts import printing


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


def main():
    name = printing.greeting()
    has_win = play_even_game()
    printing.print_result(name, has_win)


if __name__ == '__main__':
    main()
