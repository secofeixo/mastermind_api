from context.mastermind.infrastructure.game_repository import IGameRepository
from context.mastermind.command.add_guess.add_guess_dto import AddGuessDto
from context.mastermind.domain.guess import GuessResult


class AddGuessCommand:
    game_repository: IGameRepository

    def __init__(self, game_repository: IGameRepository):
        self.game_repository = game_repository
        pass

    def run(self, add_guess_dto: AddGuessDto) -> GuessResult:
        game = self.game_repository.get_game_by_id(add_guess_dto.game_id)
        guess_result = game.add_guess(add_guess_dto.code)
        self.game_repository.save(game)
        return guess_result
