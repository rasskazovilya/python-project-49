#!/usr/bin/env python3
from brain_games import logic
from brain_games.games import prime_game


def main():
    game_condition = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )
    logic.engine(prime_game, game_condition)


if __name__ == '__main__':
    main()