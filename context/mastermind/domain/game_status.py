from enum import Enum


class GAME_STATUS(str, Enum):
    PLAYING = "Playing"
    WON = "Won"
    LOST = "Lost"
