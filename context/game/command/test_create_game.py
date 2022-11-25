from context.game.command.createGame import CreateGameCommand
from context.game.infrastructure.gameRepositoryInMemory import GameRepositoryInMemory
from context.game.mappers.gameDTO import GameDTO
import uuid
import pytest

gameRepository = GameRepositoryInMemory()


def test_creating_game_command():
    game_dto = GameDTO(game_id=str(uuid.uuid4()), num_guesses=5)
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(Exception):
        commando.run(game_dto)
        assert False

    assert True


def test_creating_game_with_wrong_data():
    game_dto = GameDTO(game_id=str(uuid.uuid4()), num_guesses=5, secret_code=111111)
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(Exception) as exception:
        commando.run(game_dto)
        assert str(exception) == 'Sorry the game is over'

    assert True