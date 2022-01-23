# SEEMS TESTED
from constants import BOARD_W, BOARD_H, MAX_BLOCK_HEIGHT


# center of board, at the top of visible board (with enough place for)
# change for constant

class BlockFalling:
    # constructor
    def __init__(self, block, width=BOARD_W, height=BOARD_H):
        self.location = (width//2, height + MAX_BLOCK_HEIGHT // 2)
        self._block = block

    def execute_operation(self, operation):
        """
        Execute operation 'operation' on self, strategy design pattern
        """
        operation.change_position(self)

    def get_blocks(self):
        """
        Returns relations of squares to center of this tetris block

        Returned: relations of squares to center of this tetris block
        """
        return self._block.get_blocks()

    def blocks_on_board(self):
        """
        Returns positions squares of this tetris block on board

        Returned: positions squares of this tetris block on board
        """
        x1, y1 = self.location
        return tuple((x1 + x2, y1 + y2) for x2, y2 in self._block.get_blocks())

    def get_color(self):
        """
        Returns color of parameter _block

        Returned: color of _block
        """
        return self._block.color

    def get_inner_block(self):
        """
        Returns value of parameter _block

        Returned: value of _block
        """
        return self._block
