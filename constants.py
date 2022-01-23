from enum import Enum

BOARD_W = 10
BOARD_H = 20


SECOND_IN_MILIS = 1000


MAX_BLOCK_HEIGHT = 4


class Color(Enum):
    BLACK = (0, 0, 0)
    CYAN = (0, 238, 238)
    DARK_BLUE = (0, 0, 205)
    ORANGE = (255, 127, 36)
    YELLOW = (255, 215, 0)
    GREEN = (0, 201, 87)
    PURPLE = (148, 0, 211)
    RED = (255, 48, 48)


DIFFICULTIES_MULTIPLIERS = {
    "1": 1,
    "2": 2,
    "3": 5,
}

PYGAME_TEXT_SIZE = 12
PYGAME_TEXT_LOCATION = 10, 10

TETRIS_BLOCK_WIDTH = 20
