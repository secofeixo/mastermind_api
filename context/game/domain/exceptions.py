from shared.base_exception import BaseException


class GameOverException(BaseException):
    def __init__(self, message: str):
        super().__init__(type="GameOverException", message=message)


class GameWonException(BaseException):
    def __init__(self, message: str):
        super().__init__(type="GameWonException", message=message)


class CodeWrongException(BaseException):
    def __init__(self, message: str):
        super().__init__(type="CodeWrongException", message=message)


class GameAlreadyExistsException(BaseException):
    def __init__(self, message: str):
        super().__init__(type="GameAlreadyExistsException", message=message)


class GameNotExistsException(BaseException):
    def __init__(self, message: str):
        super().__init__(type="GameNotExistsException", message=message)
