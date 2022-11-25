from context.game.domain.SecretCode import SecretCode


def test_default_code():
    secret_code = SecretCode.create()
    assert secret_code.code == 'RBBR'


def test_new_code():
    secret_code = SecretCode.create('AAAA')
    assert secret_code.code == 'AAAA'


def test_not_enough_colors():
    secret_code = SecretCode.create('AAA')
    assert secret_code.code != 'AAA'


def test_too_much_colors():
    secret_code = SecretCode.create('AAABBBBBB')
    assert secret_code.code == 'AAAB'
    assert secret_code.code != 'AAABBBBBB'


def test_codes_equals():
    secret_code = SecretCode.create()
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
