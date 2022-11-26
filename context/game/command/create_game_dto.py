from dataclasses import dataclass
from typing import Optional


@dataclass
class CreateGameDTO:
    secret_code: Optional[str] = None
    num_max_guesses: Optional[int] = 10
