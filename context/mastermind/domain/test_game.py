import pytest
from context.mastermind.domain.game import Game, GAME_STATUS
from context.mastermind.domain.exceptions import GameOverException, GameWonException


def test_game():
    game = Game(10, 'RBRB')
    assert game.status == GAME_STATUS.PLAYING
    assert game.num_guesses == 10
    assert game.secret_code.code == 'RBRB'
    assert game.success_guess is False
    assert game.guesses == []


def test_invalid_code():
    game = None
    try:
        game = Game(10, 111)
    except Exception as e:
        assert str(e) == 'Code is not a valid string'
    finally:
        assert game is None


def test_add_wrong_guess_and_exceeding_limit():
    game = Game(1, 'RBRB')
    assert game.status == GAME_STATUS.PLAYING
    # guess = Guess.create('BBBB') maybe better to create guess entity and check the entity??
    guess_result = game.add_guess('BBBB')
    assert guess_result.correct is False
    assert guess_result.black_pegs == 2
    assert guess_result.white_pegs == 0
    assert len(game.guesses) == 1

    # adding second guess when limit is 1
    with pytest.raises(GameOverException) as exception:
        game.add_guess('BBBB')
    assert str(exception.value) == 'Sorry the game is over'
    assert game.status == GAME_STATUS.LOST


def test_add_correct_guess_and_trying_new_guess():
    game_correct = Game(2, 'RBRB')
    assert game_correct.status == GAME_STATUS.PLAYING
    # guess = Guess.create('BBBB') maybe better to create guess entity and check the entity??
    guess_result = game_correct.add_guess('RBRB')
    assert guess_result.correct is True
    assert guess_result.black_pegs == 4
    assert guess_result.white_pegs == 0
    assert len(game_correct.guesses) == 1
    assert game_correct.success_guess is True
    # test_after_correct_guess
    with pytest.raises(GameWonException) as exception:
        game_correct.add_guess('RBBR')
    assert str(exception.value) == 'Secret code already found'

    assert game_correct.status == GAME_STATUS.WON
