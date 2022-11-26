from context.game.infrastructure.gameRepositoryInMemory import GameRepositoryInMemory
from context.game.domain.Game import Game
from context.game.domain.Guess import Guess
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
    game_repository.addGame(game)
    num_games = len(game_repository.games.keys())
    assert num_games == 1


def test_add_guess_to_game():
    guess = Guess.create('AAAA')
    game_repository.addGuess(game, guess)
    num_games = len(game_repository.games.keys())
    assert num_games == 1
    assert len(game.guesses) == 1


def test_get_game():
    game_to_get = Game(game_id=game.game_id)
    game_read = game_repository.getGame(game_to_get)
    assert game_read.game_id == game.game_id
    assert len(game_read.guesses) == len(game.guesses)


def test_get_wrong_game():
    uuid4 = str(uuid.uuid4())
    game_to_get = Game(game_id=uuid4)
    with pytest.raises(GameNotExistsException) as exception:
        game_repository.getGame(game_to_get)
    assert str(exception.value) == f'Game {uuid4} doesn\'t exists'
