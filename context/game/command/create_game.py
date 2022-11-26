from context.game.infrastructure.game_repository import IGameRepository
from context.game.command.create_game_dto import CreateGameDTO
from context.game.domain.game import Game


class CreateGameCommand:
    game_repository: IGameRepository

    def __init__(self, game_repository: IGameRepository):
        self.game_repository = game_repository
        pass

    def run(self, gameDTO: CreateGameDTO) -> Game:
        game = Game(number_guesses=gameDTO.num_max_guesses,
                    secret_code=gameDTO.secret_code)
        game_entity = self.game_repository.save(game)
        return game_entity
