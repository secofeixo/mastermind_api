from context.game.mappers.guessDTO import GuessDTO
from context.game.domain.exceptions import CodeWrongException
import pytest


def test_creating_dto():
    guess_dto = GuessDTO(code='AADB')
    guess = guess_dto.toValueObject()
    assert guess.code == guess_dto.code == 'AADB'
    new_guess_dto = GuessDTO()
    new_guess_dto.fromValueObject(guess)
    assert new_guess_dto.code == guess_dto.code == 'AADB'


def test_creating_wrong_dto():
    guess_dto = GuessDTO(code=511)
    with pytest.raises(CodeWrongException) as exception:
        guess_dto.toValueObject()
    assert str(exception.value) == 'Code is not a valid string'
