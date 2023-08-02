from brain_games import cli


def ask_question(question):

    print('Question: {}'.format(question))


def is_answer_correct(answer, correct_answer):

    is_correct = answer == correct_answer

    if is_correct:
        print('Correct!')
    else:
        print(
            '\'{}\' is wrong answer ;(.'.format(answer),
            'Correct answer was \'{}\''.format(correct_answer)
        )

    return is_correct


def greeting():

    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    return name


def print_result(name, has_win):
    if has_win:
        print('Congratulations, {}!'.format(name))
    else:
        print('Let\'s try again, {}!'.format(name))


def play_game(game_fn):

    for _ in range(3):
        question, correct_answer = game_fn()

        ask_question(question)
        answer = input('Your answer: ')

        if not is_answer_correct(answer, correct_answer):
            return False

    return True


def engine(game_fn):
    name = greeting()
    has_win = play_game(game_fn)
    print_result(name, has_win)
