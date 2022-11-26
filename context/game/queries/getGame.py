from context.game.infrastructure.gameRepository import IGameRepository
from context.game.mappers.gameDTO import GameDTO


class GetGameQuery:
    game_repository: IGameRepository

    def __init__(self, game_repository: IGameRepository):
        self.game_repository = game_repository
        pass

    def run(self, gameDTO: GameDTO) -> GameDTO:
        game_to_get = gameDTO.toEntity()
        game = self.game_repository.getGame(game_to_get)
        game_result_dto = GameDTO()
        game_result_dto.fromEntity(game)
        return game_result_dto
