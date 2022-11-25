from __future__ import annotations
from typing import Optional
from SecretCode import SecretCode
from Guess import Guess, GuessResult


class Game():  # AggregateRoot or Entity
    def __init__(self, number_guesses: int, secret_code: Optional[str] = None):
        self.num_guesses = number_guesses
        self.secret_code = SecretCode.create(secret_code)
        self.guesses = []
        self.success_guess = False

    def add_guess(self, code: str) -> GuessResult:
        if len(self.guesses) > self.num_guesses:
            raise Exception("Sorry the game is over")

        if self.success_guess:
            raise Exception("Secret code already found")

        guess = Guess.create(code)
        self.success_guess = guess.verify_guess(self.secret_code)
        self.guesses.append(guess)
        return guess.guess_result
