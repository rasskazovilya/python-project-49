#!/usr/bin/env python3
from brain_games import logic
from brain_games.games import gcd_game


def main():
    game_condition = 'Find the greatest common divisor of given numbers.'
    logic.engine(gcd_game, game_condition)


if __name__ == '__main__':
    main()
