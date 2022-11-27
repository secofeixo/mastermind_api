from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional
from context.mastermind.domain.game_status import GAME_STATUS
from context.mastermind.domain.game import Game


class GuessResult(BaseModel):
    black_pegs: int
    white_pegs: int
    correct: bool
    current_status: Optional[GAME_STATUS] = GAME_STATUS.PLAYING


class GuessElement(BaseModel):
    code: str
    guess_result: GuessResult


class ResponseGetGame(BaseModel):
    game_id: str
    secret_code: str
    status: GAME_STATUS
    num_guesses: int
    guesses: List[GuessElement]
    success_guess: bool

    @staticmethod
    def fromEntity(game: Game) -> ResponseGetGame:
        list_guesses = []
        for guess_in_game in game.guesses:
            guess_result = GuessResult(black_pegs=guess_in_game.guess_result.black_pegs,
                                       white_pegs=guess_in_game.guess_result.white_pegs,
                                       correct=guess_in_game.guess_result.correct,
                                       current_status=guess_in_game.guess_result.current_status)
            guess = GuessElement(code=guess_in_game.code.code,
                                 guess_result=guess_result)
            list_guesses.append(guess)
        return ResponseGetGame(
            game_id=game.game_id,
            secret_code=game.secret_code.code,
            status=game.status,
            num_guesses=game.num_guesses,
            success_guess=game.success_guess,
            guesses=list_guesses
        )
