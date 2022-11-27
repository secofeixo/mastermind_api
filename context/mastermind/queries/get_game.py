from context.mastermind.infrastructure.game_repository import IGameRepository
from context.mastermind.domain.game import Game


class GetGameQuery:
    game_repository: IGameRepository

    def __init__(self, game_repository: IGameRepository):
        self.game_repository = game_repository

    def run(self, game_id: str) -> Game:
        return self.game_repository.get_game_by_id(game_id=game_id)
