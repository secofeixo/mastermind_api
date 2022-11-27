from context.mastermind.domain.guess import Guess
from context.mastermind.domain.secret_code import SecretCode


def test_default_guess():
    guess = Guess.create('RBBR', length_code=4)
    assert guess.code.code == 'RBBR'
    assert guess.guess_result.black_pegs == 0
    assert guess.guess_result.white_pegs == 0
    assert guess.guess_result.correct is False


def test_checking_guess_with_secret_code():
    guess = Guess.create('RBBR', length_code=4)
    secret_code = SecretCode.create('RBBR')
    guess.verify_guess(secret_code)
    assert guess.guess_result.correct is True
    assert guess.guess_result.black_pegs == 4
    assert guess.guess_result.white_pegs == 0


def test_creating_guess_with_int():
    guess = None
    try:
        guess = Guess.create(1111, length_code=4)
    except Exception as e:
        assert str(e) == 'Code is not a valid string'
    finally:
        assert guess is None


def test_checking_incorrect_guess_with_secret_code():
    secret_code = SecretCode.create('RBRB', length=4)
    guess = Guess.create('RBRR', length_code=4)
    guess.verify_guess(secret_code)
    print(secret_code, guess)
    assert guess.guess_result.correct is False
    assert guess.guess_result.black_pegs == 3
    assert guess.guess_result.white_pegs == 1


def test_checking_guess_one_but_in_wrong_position():
    secret_code = SecretCode.create('RBRB', length=4)
    guess = Guess.create('YYYB', length_code=4)
    guess.verify_guess(secret_code)
    print(secret_code, guess)
    assert guess.guess_result.correct is False
    assert guess.guess_result.black_pegs == 1
    assert guess.guess_result.white_pegs == 1


def test_checking_guess_four_but_in_wrong_position():
    secret_code = SecretCode.create('YRBW', length=4)
    guess = Guess.create('WBRY', length_code=4)
    guess.verify_guess(secret_code)
    print(secret_code, guess)
    assert guess.guess_result.correct is False
    assert guess.guess_result.black_pegs == 0
    assert guess.guess_result.white_pegs == 4
