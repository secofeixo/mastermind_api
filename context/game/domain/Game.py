from __future__ import annotations
from typing import Optional
from context.game.domain.SecretCode import SecretCode
from context.game.domain.Guess import Guess, GuessResult
import uuid


class Game():  # AggregateRoot or Entity
    def __init__(self, number_guesses: Optional[int] = 10, secret_code: Optional[str] = None, game_id: Optional[str] = None):
        self.num_guesses = number_guesses
        self.secret_code = SecretCode.create(secret_code)
        self.guesses = []
        self.success_guess = False
        self.game_id = game_id if game_id is not None else self.generate_game_id()

    @staticmethod
    def generate_game_id() -> str:
        return str(uuid.uuid4())

    def add_guess(self, code: str) -> GuessResult:
        if len(self.guesses) > self.num_guesses:
            raise Exception("Sorry the game is over")

        if self.success_guess:
            raise Exception("Secret code already found")

        guess = Guess.create(code)
        self.success_guess = guess.verify_guess(self.secret_code)
        self.guesses.append(guess)
        return guess.guess_result
