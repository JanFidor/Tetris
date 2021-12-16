# SEEMS TESTED
from board import BOARD_H, BOARD_W


# center of board, at the top of visible board (with enough place for)
# change for constant
STARTING_LOCATION = (BOARD_W // 2, BOARD_H - 2)


class BlockFalling:
    def __init__(self, block, width=BOARD_W, height=BOARD_H):
        self.location = (width//2, height + 2)
        self._block = block

    def execute_operation(self, move):
        move.change_position(self)

    def get_blocks(self):
        return self._block.get_blocks()

    def blocks_on_board(self):
        x1, y1 = self.location
        return tuple((x1 + x2, y1 + y2) for x2, y2 in self._block.get_blocks())

    def get_color(self):
        return self._block.color

    def get_inner_block(self):
        return self._block
