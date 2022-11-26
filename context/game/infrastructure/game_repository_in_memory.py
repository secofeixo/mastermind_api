from context.game.infrastructure.game_repository import IGameRepository
from context.game.domain.game import Game
from context.game.domain.guess import Guess, GuessResult
from context.game.domain.exceptions import GameNotExistsException


class GameRepositoryInMemory(IGameRepository):
    games: dict

    def __init__(self):
        self.games = {}

    def save(self, game: Game) -> Game:
        self.games[game.game_id] = game
        return self.games[game.game_id]

    def add_guess(self, game: Game, guess: Guess) -> GuessResult:
        if game.game_id not in self.games:
            raise GameNotExistsException(f'Game {game.game_id} doesn\'t exists')

        guess_result = self.games[game.game_id].add_guess(guess.code)
        return guess_result

    def get_game_by_id(self, game_id: str) -> Game:
        if game_id not in self.games:
            raise GameNotExistsException(f'Game {game_id} doesn\'t exists')

        return self.games[game_id]
