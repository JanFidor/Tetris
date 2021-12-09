
class BlockNotAddedError(Exception):
    def __init__(self):
        super().__init__("Block not added to BlockFallingManager")


BOARD_W = 10
BOARD_H = 20


class Board:
    def __init__(self, width=BOARD_W, height=BOARD_H):
        self._width = width
        self._height = height
        self._board = [[None for _ in range(width)] for _ in range(height + 4)]

    def is_above_board(self, block):
        for x, y in block.blocks_on_board():
            if y >= self._height:
                return True
        return False

    def _iterate_condition(self, positions):
        # loc_x, loc_y = self._block.get_location()
        for block_x, block_y in positions:
            if not self._existance_condition(block_x, block_y):
                return False
        return True

    def can_go_left(self, block):
        blocks = ((x - 1, y) for x, y in block.blocks_on_board())
        return self._iterate_condition(blocks)

    def can_go_right(self, block):
        blocks = ((x + 1, y) for x, y in block.blocks_on_board())
        return self._iterate_condition(blocks)

    def can_go_down(self, block):
        blocks = ((x, y - 1) for x, y in block.blocks_on_board())
        return self._iterate_condition(blocks)

    def _existance_condition(self, x, y):
        return 0 <= x <= BOARD_W and y >= 0 and self._board[y][x] is None

    def _can_turn(self, location, new_position):
        loc_x, loc_y = location
        blocks = ((loc_x + x, loc_y + y) for x, y in new_position)
        return self._iterate_condition(blocks)

    def can_turn_left(self, block):
        location = block.get_location()
        new_position = block._block.get_left_position()
        return self._can_turn(location, new_position)

    def can_turn_right(self, block):
        location = block.get_location()
        new_position = block._block.get_right_position()
        return self._can_turn(location, new_position)
