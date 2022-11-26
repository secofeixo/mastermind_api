from context.game.command.createGame import CreateGameCommand
from context.game.command.addGuess import AddGuessCommand
from context.game.infrastructure.gameRepositoryInMemory import GameRepositoryInMemory
from context.game.mappers.gameDTO import GameDTO
from context.game.mappers.guessDTO import GuessDTO
import uuid
import pytest

gameRepository = GameRepositoryInMemory()
game_dto = None
game = None


def test_creating_game_command():
    global game_dto
    global game
    game_dto = GameDTO(game_id=str(uuid.uuid4()), num_guesses=3, secret_code='AAAA')
    commando = CreateGameCommand(gameRepository)
    with pytest.raises(Exception):
        game = commando.run(game_dto)
        assert False

    assert True


def test_adding_wrong_guess():
    guess_dto = GuessDTO(code='BBBB')
    commando = AddGuessCommand(gameRepository)
    result = commando.run(game_dto, guess_dto)
    assert result.black_pegs == 0
    assert result.white_pegs == 0
    assert result.correct is False


def test_adding_correct_guess():
    guess_dto = GuessDTO(code='AAAA')
    commando = AddGuessCommand(gameRepository)
    result = commando.run(game_dto, guess_dto)
    assert result.black_pegs == 0
    assert result.white_pegs == 0
    assert result.correct is True
