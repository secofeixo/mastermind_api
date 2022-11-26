from context.game.infrastructure.game_repository_in_memory import GameRepositoryInMemory
from context.game.domain.game import Game
from context.game.domain.exceptions import GameNotExistsException
import uuid
import pytest

game_repository = GameRepositoryInMemory()


def test_creating_empty_repository():
    assert game_repository.games == {}
    num_games = len(game_repository.games.keys())
    assert num_games == 0


game = Game(10, 'ABRB')


def test_add_new_game():
    game_repository.save(game)
    num_games = len(game_repository.games.keys())
    assert num_games == 1


def test_add_guess_to_game():
    game.add_guess('AAAA')
    game_repository.save(game)
    num_games = len(game_repository.games.keys())
    assert num_games == 1
    assert len(game.guesses) == 1


def test_get_game():
    game_read = game_repository.get_game_by_id(game.game_id)
    assert game_read.game_id == game.game_id
    assert len(game_read.guesses) == len(game.guesses)


def test_get_wrong_game():
    game_id = str(uuid.uuid4())
    with pytest.raises(GameNotExistsException) as exception:
        game_repository.get_game_by_id(game_id)
    assert str(exception.value) == f'Game {game_id} doesn\'t exists'
