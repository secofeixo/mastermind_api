from context.game.infrastructure.gameRepository import IGameRepository
from context.game.domain.Game import Game
from context.game.domain.Guess import Guess


class GameRepositoryInMemory(IGameRepository):
    def __init__(self):
        self.games = {}

    def addGame(self, game: Game):
        if game.game_id in self.games:
            raise (f'Game {game.game_id} already exists')
        self.games[game.game_id] = game

    def addGuess(self, game: Game, guess: Guess):
        if game.game_id not in self.games:
            raise (f'Game {game.game_id} doesn\'t exists')

        self.games[game.game_id].add_guess(guess.code)
        return self.games[game.game_id]

    def getGame(self, game: Game) -> Game:
        if game.game_id not in self.games:
            raise (f'Game {game.game_id} doesn\'t exists')

        return self.games[game.game_id]
