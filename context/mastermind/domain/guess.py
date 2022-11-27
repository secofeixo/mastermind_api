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
        self.guess_result: GuessResult = GuessResult()

    def verify_guess(self, secret_code: SecretCode) -> bool:

        for index, color in enumerate(secret_code.code):
            if any(color == c for c in self.code.code):
                if secret_code.code[index] == self.code.code[index]:
                    self.guess_result.black_pegs += 1
                else:
                    self.guess_result.white_pegs += 1

        self.guess_result.correct = self.guess_result.black_pegs == 4
        return self.guess_result.correct

    @classmethod
    def create(self, code: str, length_code: int) -> Guess:
        secret_code = SecretCode.create(code, length_code)

        # all will be uppercase
        return self(secret_code)


class GuessResult():
    black_pegs: int
    white_pegs: int
    correct: bool
    current_status: Optional[GAME_STATUS] = GAME_STATUS.PLAYING

    def __init__(self,
                 black_pegs: int = 0,
                 white_pegs: int = 0,
                 correct: bool = False,
                 status: Optional[GAME_STATUS] = GAME_STATUS.PLAYING):
        self.black_pegs = black_pegs
        self.white_pegs = white_pegs
        self.correct = correct
        self.current_status = status
