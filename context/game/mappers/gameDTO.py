from __future__ import annotations
from typing import Optional, List
from context.game.domain.Game import Game
from context.game.mappers.guessDTO import GuessDTO


class GameDTO:
    game_id: str
    num_guesses: int = 10
    secret_code: str
    status: str
    guesses: List[GuessDTO]

    def __init__(self,
                 game_id: Optional[str] = None,
                 num_guesses: Optional[int] = 10,
                 secret_code: Optional[str] = None,
                 status: Optional[str] = None):
        self.game_id = game_id
        self.num_guesses = num_guesses
        self.secret_code = secret_code
        self.status = status
        self.guesses = []

    def toEntity(self) -> Optional[Game]:
        game = Game(self.num_guesses, self.secret_code, game_id=self.game_id, status=self.status)
        for guess in self.guesses:
            game.add_guess(guess.code)
        return game

    def fromEntity(self, game: Game) -> GameDTO:
        self.game_id = game.game_id
        self.num_guesses = game.num_guesses
        self.secret_code = game.secret_code.code
        self.status = game.status
        self.guesses.clear()
        for guess_vo in game.guesses:
            guess_dto = GuessDTO(guess_vo.code)
            self.guesses.append(guess_dto)
        return self
