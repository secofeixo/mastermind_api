from typing import Optional
from context.game.domain.Guess import Guess, GuessResult


class GuessDTO:
    code: str

    def __init__(self, code: str):
        self.code = code

    def toValueObject(self) -> Optional[Guess]:
        return Guess.create(self.code)

    def fromValueObject(self, guess: Guess):
        self.code = guess.code


class GuessResultDTO:
    black_pegs: int
    white_pegs: int
    correct: bool

    def fromValueObject(self, guess_result: GuessResult):
        self.black_pegs = guess_result.black_pegs
        self.white_pegs = guess_result.white_pegs
        self.correct = guess_result.correct
