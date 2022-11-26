from context.game.command.create_game import CreateGameCommand
from context.game.infrastructure.game_repository_in_memory import GameRepositoryInMemory
from context.game.command.create_game_dto import CreateGameDTO
from context.game.domain.exceptions import CodeWrongException
import pytest

gameRepository = GameRepositoryInMemory()


def test_creating_game_command():
    create_dto = CreateGameDTO(num_max_guesses=5)
    commando = CreateGameCommand(gameRepository)
    game = None
    with pytest.raises(Exception):
        game = commando.run(create_dto)
        assert False

    assert game.num_guesses == 5


def test_creating_game_with_wrong_data():
    create_dto = CreateGameDTO(num_max_guesses=5, secret_code=111111)
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(CodeWrongException) as exception:
        commando.run(create_dto)
    assert str(exception.value) == 'Code is not a valid string'
