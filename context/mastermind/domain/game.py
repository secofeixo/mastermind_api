from __future__ import annotations
from typing import Optional, List
from context.mastermind.domain.secret_code import SecretCode
from context.mastermind.domain.guess import Guess, GuessResult
from context.mastermind.domain.exceptions import GameOverException, GameWonException
from context.mastermind.domain.game_status import GAME_STATUS
import uuid


class Game():  # AggregateRoot or Entity
    num_guesses: int
    secret_code: SecretCode
    length_secret_code: int
    guesses: List[Guess]
    success_guess: bool
    game_id: str
    status: GAME_STATUS

    def __init__(self,
                 number_guesses: Optional[int] = 10,
                 secret_code: Optional[str] = None,
                 game_id: Optional[str] = None,
                 status: Optional[GAME_STATUS] = None,
                 length_code: Optional[int] = 4):
        self.num_guesses = number_guesses
        self.secret_code = SecretCode.create(secret_code)
        self.guesses = []
        self.success_guess = False
        self.game_id = game_id if game_id is not None else self.generate_game_id()
        self.status = GAME_STATUS.PLAYING if status is None else status
        self.length_secret_code = length_code

    @staticmethod
    def generate_game_id() -> str:
        return str(uuid.uuid4())

    def add_guess(self, code: str) -> GuessResult:
        if self.status == GAME_STATUS.LOST:
            raise GameOverException("Sorry the game is over")

        if self.status == GAME_STATUS.WON:
            raise GameWonException("Secret code already found")

        guess = Guess.create(code, self.length_secret_code)
        self.success_guess = guess.verify_guess(self.secret_code)
        self.guesses.append(guess)

        if (self.success_guess):
            self.status = GAME_STATUS.WON

        if (len(self.guesses) >= self.num_guesses):
            self.status = GAME_STATUS.LOST

        guess.guess_result.current_status = self.status

        return guess.guess_result
