from pydantic import BaseModel
from context.mastermind.domain.game_status import GAME_STATUS


class AddGuessDto(BaseModel):
    game_id: str
    code: str


class AddGuessBody(BaseModel):
    code: str


class ResponseAddGuess(BaseModel):
    black_pegs: int
    white_pegs: int
    correct: bool
    status: GAME_STATUS
