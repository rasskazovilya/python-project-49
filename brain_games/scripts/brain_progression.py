#!/usr/bin/env python3
from brain_games import logic
from brain_games.games import progression_game


def main():
    game_condition = 'What number is missing in the progression?'
    logic.engine(progression_game, game_condition)


if __name__ == '__main__':
    main()
