from typing import Optional
from context.game.domain.Game import Game


class GameDTO:
    game_id: str
    num_guesses: int = 10
    secret_code: str

    def __init__(self,
                 game_id: Optional[str] = None,
                 num_guesses: Optional[int] = 10,
                 secret_code: Optional[str] = None):
        self.game_id = game_id
        self.num_guesses = num_guesses
        self.secret_code = secret_code

    def toEntity(self) -> Optional[Game]:
        return Game(self.num_guesses, self.secret_code, game_id=self.game_id)

    def fromEntity(self, game: Game):
        self.game_id = game.game_id
        self.num_guesses = game.num_guesses
        self.secret_code = game.secret_code
