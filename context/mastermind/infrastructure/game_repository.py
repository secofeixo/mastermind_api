from abc import ABC, abstractmethod
from context.mastermind.domain.game import Game


class IGameRepository(ABC):
    @abstractmethod
    def save(self, game: Game) -> Game:
        pass

    @abstractmethod
    def get_game_by_id(self, game_id: str) -> Game:
        pass
