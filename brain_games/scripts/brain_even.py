import random
from brain_games import cli


def is_even(num):
    return num % 2 == 0


def guess(name):

    for _ in range(3):
        rand_num = random.randint(1, 1000)
        ask_question(rand_num)

        answer = input('Your answer: ')
        correct_answer = 'yes' if is_even(rand_num) else 'no'

        if not compare_answers(answer, correct_answer):
            print('Let\'s try again, {}!'.format(name))
            return

    print('Congratulations, {}!'.format(name))
    return


def ask_question(question):

    print('Question: {}'.format(question))


def compare_answers(answer, correct_answer):

    is_answer_correct = answer == correct_answer

    if is_answer_correct:
        print('Correct!')
    else:
        print(
            '\'{}\' is wrong answer ;(.'.format(answer),
            'Correct answer was \'{}\''.format(correct_answer)
        )

    return is_answer_correct


def main():
    # Greeting
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    guess(name)


if __name__ == '__main__':
    main()
