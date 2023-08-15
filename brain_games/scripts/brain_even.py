#!/usr/bin/env python3
from brain_games import logic
from brain_games.games.even_game import even_game


def main():
    game_condition = (
        'Answer "yes" if the number is even, otherwise answer "no".'
    )
    logic.engine(even_game, game_condition)


if __name__ == '__main__':
    main()
