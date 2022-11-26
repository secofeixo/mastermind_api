from context.game.mappers.guessDTO import GuessDTO
import pytest


def test_creating_dto():
    guess_dto = GuessDTO(code='AADB')
    guess = guess_dto.toValueObject()
    assert guess.code == guess_dto.code == 'AADB'


def test_creating_wrong_dto():
    with pytest.raises(Exception) as exception:
        GuessDTO(code=511)
        assert str(exception) == 'Code is not a valid string'
