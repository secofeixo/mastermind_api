from context.game.infrastructure.gameRepository import IGameRepository
from context.game.mappers.guessDTO import GuessDTO, GuessResultDTO
from context.game.mappers.gameDTO import GameDTO


class AddGuessCommand:
    game_repository: IGameRepository

    def __init__(self, game_repository: IGameRepository):
        self.game_repository = game_repository
        pass

    def run(self, gameDTO: GameDTO, guessDTO: GuessDTO) -> GuessResultDTO:
        guess = guessDTO.toValueObject()
        game = gameDTO.toEntity()
        guess_result = self.game_repository.addGuess(game, guess)
        guess_result_dto = GuessResultDTO()
        guess_result_dto.fromValueObject(guess_result)
        return guess_result_dto
