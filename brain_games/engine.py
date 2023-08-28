from brain_games import cli


GAME_ROUNDS = 3


def engine(game_module):
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print(game_module.GAME_RULES)

    for _ in range(GAME_ROUNDS):
        question, correct_answer = game_module.game()

        print('Question: {}'.format(question))
        answer = input('Your answer: ')

        is_correct = answer == correct_answer

        if is_correct:
            print('Correct!')
            has_win = True
        else:
            print(
                '\'{}\' is wrong answer ;(.'.format(answer),
                'Correct answer was \'{}\''.format(correct_answer)
            )
            has_win = False
            break

    if has_win:
        print('Congratulations, {}!'.format(name))
    else:
        print('Let\'s try again, {}!'.format(name))
