from context.mastermind.command.create_game.create_game import CreateGameCommand
from context.mastermind.command.create_game.create_game_dto import CreateGameDTO
from context.mastermind.queries.get_game import GetGameQuery
from context.mastermind.infrastructure.game_repository_in_memory import GameRepositoryInMemory
from context.mastermind.domain.exceptions import GameNotExistsException
import pytest

gameRepository = GameRepositoryInMemory()
game_dto = None
game_result = None


def test_creating_game_command():
    global game_dto
    global game_result
    create_dto = CreateGameDTO(num_max_guesses=3, secret_code='BBBB')
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(Exception):
        game_result = commando.run(create_dto)
        assert False

    assert True


def test_getting_game():
    commando = GetGameQuery(gameRepository)
    result = commando.run(game_result.game_id)
    assert result.game_id == game_result.game_id


def test_getting_wrong_game():
    commando = GetGameQuery(gameRepository)
    game_id = '1234'
    result = None
    with pytest.raises(GameNotExistsException) as exception:
        result = commando.run(game_id=game_id)
    assert str(exception.value) == f'Game {game_id} doesn\'t exists'
    assert result is None
