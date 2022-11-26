from context.game.command.createGame import CreateGameCommand
from context.game.queries.getGame import GetGameQuery
from context.game.infrastructure.gameRepositoryInMemory import GameRepositoryInMemory
from context.game.mappers.gameDTO import GameDTO
from context.game.domain.exceptions import GameNotExistsException
import uuid
import pytest

gameRepository = GameRepositoryInMemory()
game_dto = None
game_result = None


def test_creating_game_command():
    global game_dto
    global game_result
    game_dto = GameDTO(game_id=str(uuid.uuid4()), num_guesses=3, secret_code='AAAA')
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(Exception):
        game_result = commando.run(game_dto)
        assert False

    assert True


def test_getting_game():
    commando = GetGameQuery(gameRepository)
    query_game = GameDTO(game_id=game_result.game_id)
    result = commando.run(query_game)
    assert result.game_id == game_result.game_id


def test_getting_wrong_game():
    commando = GetGameQuery(gameRepository)
    game_id = '1234'
    query_game = GameDTO(game_id=game_id)
    result = None
    with pytest.raises(GameNotExistsException) as exception:
        result = commando.run(query_game)
    assert str(exception.value) == f'Game {game_id} doesn\'t exists'
    assert result is None
