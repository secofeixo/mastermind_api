from dataclasses import dataclass


@dataclass
class AddGuessDto:
    game_id: str
    code: str
