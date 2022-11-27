from pydantic import BaseModel
from typing import Optional


class CreateGameDTO(BaseModel):
    secret_code: Optional[str] = None
    num_max_guesses: Optional[int] = 10


class CreateGameBody(BaseModel):
    code: Optional[str] = None
    num_guesses: Optional[int] = 10


class ResponseCreateGame(BaseModel):
    game_id: str
