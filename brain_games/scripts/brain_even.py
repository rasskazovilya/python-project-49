import random
from brain_games import cli


def is_even(num):
    return num % 2 == 0


def guess(name):

    for _ in range(3):
        rand_num = random.randint(1, 1000)
        print('Question: {}'.format(rand_num))

        answer = input('Your answer: ')
        correct_answer = 'yes' if is_even(rand_num) else 'no'

        if answer == correct_answer:
            print('Correct!')
        else:
            print(
                '\'{}\' is wrong answer ;(.'.format(answer),
                'Correct answer was \'{}\''.format(correct_answer)
            )
            print('Let\'s try again, {}!'.format(name))
            return

    print('Congratulations, {}!'.format(name))
    return


def main():
    # Greeting
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    guess(name)


if __name__ == '__main__':
    main()
