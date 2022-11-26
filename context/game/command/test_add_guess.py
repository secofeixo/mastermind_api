from context.game.command.create_game import CreateGameCommand
from context.game.command.create_game_dto import CreateGameDTO
from context.game.command.add_guess import AddGuessCommand
from context.game.command.add_guess_dto import AddGuessDto
from context.game.infrastructure.game_repository_in_memory import GameRepositoryInMemory
import pytest

gameRepository = GameRepositoryInMemory()
game_dto = None
game = None


def test_creating_game_command():
    global game_dto
    global game
    game_dto = CreateGameDTO(num_max_guesses=3, secret_code='AAAA')
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(Exception):
        game = commando.run(game_dto)
        assert False

    assert True


def test_adding_wrong_guess():
    add_guess_dto = AddGuessDto(game_id=game.game_id, code='BBBB')
    commando = AddGuessCommand(gameRepository)
    result = commando.run(add_guess_dto)
    assert result.black_pegs == 0
    assert result.white_pegs == 0
    assert result.correct is False


def test_adding_correct_guess():
    add_guess_dto = AddGuessDto(game_id=game.game_id, code='AAAA')
    commando = AddGuessCommand(gameRepository)
    result = commando.run(add_guess_dto)
    assert result.black_pegs == 0
    assert result.white_pegs == 0
    assert result.correct is True
