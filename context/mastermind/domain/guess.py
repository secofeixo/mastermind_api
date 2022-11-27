# value object secret code
from __future__ import annotations
from typing import Optional
from context.mastermind.domain.secret_code import SecretCode
from context.mastermind.domain.game_status import GAME_STATUS


class Guess():  # value object
    code: SecretCode
    guess_result: GuessResult

    def __init__(self, code: SecretCode):
        self.code = code
        self.guess_result: GuessResult = GuessResult(0, 0, False)

    def verify_guess(self, secret_code: SecretCode) -> bool:
        # add algorithm to get white_pegs and black_pegs
        self.guess_result.correct = secret_code.equal_to(self.code.code)
        return self.guess_result.correct

    @classmethod
    def create(self, code: str) -> Guess:
        secret_code = SecretCode.create(code)

        # all will be uppercase
        return self(secret_code)


class GuessResult():
    black_pegs: int
    white_pegs: int
    correct: bool
    current_status: Optional[GAME_STATUS] = GAME_STATUS.PLAYING

    def __init__(self,
                 black_pegs: int,
                 white_pegs: int,
                 correct: bool,
                 status: Optional[GAME_STATUS]=GAME_STATUS.PLAYING):
        self.black_pegs = black_pegs
        self.white_pegs = white_pegs
        self.correct = correct
        self.current_status = status
