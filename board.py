# NOT EVEN WIP

from generator import generate_random_block
from block_falling import BlockFalling

BOARD_W = 10
BOARD_H = 24


class Board:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_W)] for _ in range(BOARD_H)]
