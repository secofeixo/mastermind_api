from context.game.infrastructure.gameRepository import IGameRepository
from context.game.mappers.gameDTO import GameDTO


class CreateGameCommand:
    game_repository: IGameRepository

    def __init__(self, game_repository: IGameRepository):
        self.game_repository = game_repository
        pass

    def run(self, gameDTO: GameDTO):
        game = gameDTO.toEntity()
        self.game_repository.addGame(game)