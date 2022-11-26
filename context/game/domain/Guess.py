# value object secret code
from __future__ import annotations
from context.game.domain.secret_code import SecretCode
from context.game.domain.exceptions import CodeWrongException


class Guess():  # value object
    code: str
    guess_result: GuessResult

    def __init__(self, code: str):
        self.code = code
        self.guess_result: GuessResult = GuessResult(0, 0, False)

    def verify_guess(self, secret_code: SecretCode) -> bool:
        # add algorithm to get white_pegs and black_pegs
        self.guess_result.correct = secret_code.equal_to(self.code)
        return self.guess_result.correct

    @classmethod
    def create(self, code: str) -> Guess:
        if code is not None and isinstance(code, str) is False:
            raise CodeWrongException('Code is not a valid string')

        if code is None:
            return self('')

        # check str is valid string of colors
        if len(code) > 4:
            code = code[:4]

        # all will be uppercase
        return self(code.upper())


class GuessResult():
    black_pegs: int
    white_pegs: int
    correct: bool

    def __init__(self, black_pegs: int, white_pegs: int, correct: bool):
        self.black_pegs = black_pegs
        self.white_pegs = white_pegs
        self.correct = correct
