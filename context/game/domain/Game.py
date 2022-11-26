from __future__ import annotations
from enum import Enum
from typing import Optional, List
from context.game.domain.secret_code import SecretCode
from context.game.domain.guess import Guess, GuessResult
from context.game.domain.exceptions import GameOverException, GameWonException
import uuid


class GAME_STATUS(str, Enum):
    PLAYING = "Playing"
    WON = "Won"
    LOST = "Lost"


class Game():  # AggregateRoot or Entity
    num_guesses: int
    secret_code: SecretCode
    guesses: List[Guess]
    success_guess: bool
    game_id: str
    status: GAME_STATUS

    def __init__(self,
                 number_guesses: Optional[int] = 10,
                 secret_code: Optional[str] = None,
                 game_id: Optional[str] = None,
                 status: Optional[GAME_STATUS] = None):
        self.num_guesses = number_guesses
        self.secret_code = SecretCode.create(secret_code)
        self.guesses = []
        self.success_guess = False
        self.game_id = game_id if game_id is not None else self.generate_game_id()
        self.status = GAME_STATUS.PLAYING if status is None else status

    @staticmethod
    def generate_game_id() -> str:
        return str(uuid.uuid4())

    def add_guess(self, code: str) -> GuessResult:
        if self.status == GAME_STATUS.LOST:
            raise GameOverException("Sorry the game is over")

        if self.status == GAME_STATUS.WON:
            raise GameWonException("Secret code already found")

        guess = Guess.create(code)
        self.success_guess = guess.verify_guess(self.secret_code)
        self.guesses.append(guess)

        if (self.success_guess):
            self.status = GAME_STATUS.WON

        if (len(self.guesses) >= self.num_guesses):
            self.status = GAME_STATUS.LOST

        return guess.guess_result
