# CHANGE CONDITIONS AND CHANGES TO LOCATION
from board import BOARD_W


class BlockNotAddedError(Exception):
    def __init__(self):
        super().__init__("Block not added to BlockFallingManager")


class BlockFallingManager:
    def __init__(self, board):
        self._board = board
        self._block = None

    def set_block(self, block):
        self._block = block

    def remove_block(self):
        self._block = None

    def _iterate_condition(self, positions):
        loc_x, loc_y = self._block.get_location()
        for block_x, block_y in positions:
            x = block_x + loc_x
            y = block_y + loc_y
            if not self._existance_condition(x, y):
                return False
        return True

    def _is_block_added(self):
        if not self._block:
            raise(BlockNotAddedError())

    def go_left(self):
        self._is_block_added()
        if self._can_go_left():
            self._block.go_left()

    def go_right(self):
        self._is_block_added()
        if self._can_go_right():
            self._block.go_right()

    def go_down(self):
        self._is_block_added()
        if self._can_go_down():
            self._block.go_down()

    def turn_left(self):
        self._is_block_added()
        if self._can_turn_left():
            self._block.turn_left()

    def turn_right(self):
        self._is_block_added()
        if self._can_turn_right():
            self._block.turn_right()

    def _can_go_left(self):
        blocks = ((x - 1, y) for x, y in self._block.blocks_on_board())
        return self._iterate_condition(blocks)

    def _can_go_right(self):
        blocks = ((x + 1, y) for x, y in self._block.blocks_on_board())
        return self._iterate_condition(blocks)

    def _can_go_down(self):
        blocks = ((x, y - 1) for x, y in self._block.blocks_on_board())
        return self._iterate_condition(blocks)

    def _existance_condition(self, x, y):
        return 0 <= x <= BOARD_W and y >= 0 and self._board[y][x] == 0

    def _can_turn(self, new_position):
        loc_x, loc_y = self._block.get_location
        blocks = ((loc_x + x, loc_y + y) for x, y in new_position)
        return self._iterate_condition(blocks)

    def _can_turn_left(self):
        new_position = self._block.get_left_position()
        return self._can_turn(new_position)

    def _can_turn_right(self):
        new_position = self._block.get_right_position()
        return self._can_turn(new_position)
