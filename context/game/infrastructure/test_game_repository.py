from context.game.infrastructure.gameRepositoryInMemory import GameRepositoryInMemory
from context.game.domain.Game import Game
from context.game.domain.Guess import Guess


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
    game_read = game_repository.getGame(game)
    assert len(game_read.guesses) == 1


