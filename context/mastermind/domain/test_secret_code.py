from context.mastermind.domain.secret_code import SecretCode, GuessColor


def test_default_code():
    secret_code = SecretCode.create()
    guess_color_list = list(GuessColor)
    for c in secret_code.code:
        assert c in guess_color_list


def test_new_code():
    secret_code = SecretCode.create('BBBB')
    assert secret_code.code == 'BBBB'


def test_not_enough_colors():
    secret_code = SecretCode.create('BBB')
    assert secret_code.code != 'BBB'


def test_too_much_colors():
    secret_code = SecretCode.create('RRRBBBBBB')
    assert secret_code.code == 'RRRB'
    assert secret_code.code != 'RRRBBBBBB'


def test_codes_equals():
    secret_code = SecretCode.create('RBBR')
    assert secret_code.equal_to('RBBR') is True
    assert secret_code.equal_to('BBR') is False


def test_passing_no_string():
    secret_code = None
    try:
        secret_code = SecretCode.create(11111)
    except Exception as e:
        assert str(e) == 'Code is not a valid string'
    finally:
        assert secret_code is None


def test_wrong_color():
    secret_code = None
    try:
        secret_code = SecretCode.create('AAAA')
    except Exception as e:
        assert str(e) == 'Code is not a valid string'
    finally:
        assert secret_code is None
