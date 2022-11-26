from context.game.domain.guess import Guess
from context.game.domain.secret_code import SecretCode


def test_default_guess():
    guess = Guess.create('RBBR')
    assert guess.code == 'RBBR'
    assert guess.guess_result.black_pegs == 0
    assert guess.guess_result.white_pegs == 0
    assert guess.guess_result.correct is False


def test_checking_guess_with_secret_code():
    guess = Guess.create('RBBR')
    secret_code = SecretCode.create()
    guess.verify_guess(secret_code)
    assert guess.guess_result.correct is True
    assert guess.guess_result.black_pegs == 0
    assert guess.guess_result.white_pegs == 0


def test_creating_guess_with_int():
    guess = None
    try:
        guess = Guess.create(1111)
    except Exception as e:
        assert str(e) == 'Code is not a valid string'
    finally:
        assert guess is None


def test_checking_incorrect_guess_with_secret_code():
    secret_code = SecretCode.create('RBRB')
    guess = Guess.create('RBRR')
    guess.verify_guess(secret_code)
    print(secret_code, guess)
    assert guess.guess_result.correct is False
    assert guess.guess_result.black_pegs == 0
    assert guess.guess_result.white_pegs == 0
