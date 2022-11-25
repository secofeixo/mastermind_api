# value object secret code
from __future__ import annotations
from typing import Optional


class SecretCode():  # value object
    def __init__(self, code: str):
        self.code = code

    def equal_to(self, code: str) -> bool:
        return self.code == code

    @staticmethod
    def generate_secret_code() -> str:
        return 'RBBR'

    @classmethod
    def create(self, code: Optional[str] = None) -> SecretCode:
        if code is not None and isinstance(code, str) is False:
            raise Exception('Code is not a valid string')

        if code is None or len(code) < 4:
            code = SecretCode.generate_secret_code()

        # check str is valid string of colors
        if len(code) > 4:
            code = code[:4]

        # all will be uppercase
        return self(code.upper())
