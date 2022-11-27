# value object secret code
from __future__ import annotations
import random
from enum import Enum
from typing import Optional
from context.mastermind.domain.exceptions import CodeWrongException


class GuessColor(str, Enum):
    RED = "R"
    YELLOW = "Y"
    ORANGE = "O"
    BLUE = "B"
    PINK = "P"
    GREEN = "G"
    WHITE = "W"
    MAGENTA = "M"

    def __str__(self) -> str:
        return self.value


class SecretCode():  # value object
    code: str
    length: int

    def __init__(self, code: str, length: Optional[int] = 4):
        self.code = code
        self.length = length

    def equal_to(self, code: str) -> bool:
        return self.code == code

    @staticmethod
    def generate_secret_code(code_length: Optional[int] = 4) -> str:
        code = ''

        for i in range(code_length):
            code += random.choice(list(GuessColor))
        return code

    @classmethod
    def create(self, code: Optional[str] = None, length: int = 4) -> SecretCode:
        if code is not None and isinstance(code, str) is False:
            raise CodeWrongException('Code is not a valid string')

        if code is None or len(code) < length:
            code = SecretCode.generate_secret_code(code_length=length)
            return self(code)

        guess_color_list = list(GuessColor)
        for char in code:
            if char not in guess_color_list:
                raise CodeWrongException('Code is not a valid string')

        # check str is valid string of colors
        if len(code) > length:
            code = code[:length]

        # all will be uppercase
        return self(code.upper())
