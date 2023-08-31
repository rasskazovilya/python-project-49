from brain_games import cli


GAME_ROUNDS = 3


def run(game_module):
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(game_module.GAME_RULES)

    for _ in range(GAME_ROUNDS):
        question, correct_answer = game_module.play()

        print('Question: {}'.format(question))
        answer = input('Your answer: ')

        is_correct = answer == correct_answer

        if not is_correct:
            print(
                '\'{}\' is wrong answer ;(.'.format(answer),
                'Correct answer was \'{}\''.format(correct_answer),
                'Let\'s try again, {}!'.format(name)
            )
            return
        print('Correct!')

    print('Congratulations, {}!'.format(name))
