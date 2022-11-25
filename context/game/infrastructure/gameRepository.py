from abc import ABC, abstractmethod
from context.game.domain.Game import Game
from context.game.domain.Guess import Guess


class IGameRepository(ABC):
    @abstractmethod
    def addGame(self, game: Game):
        pass

    @abstractmethod
    def addGuess(self, game: Game, guess: Guess):
        pass

    @abstractmethod
    def getGame(self, game: Game) -> Game:
        pass
