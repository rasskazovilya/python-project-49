#!/usr/bin/env python3
from brain_games import logic
from brain_games.games.calc_game import calc_game


def main():
    game_condition = 'What is the result of the expression?'
    logic.engine(calc_game, game_condition)


if __name__ == '__main__':
    main()
