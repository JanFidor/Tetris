
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

    def land_block(self, block):
        for x, y in block.blocks_on_board():
            self._board[y][x] = block.get_color()

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

    def _existance_condition(self, x, y):
        return 0 <= x <= BOARD_W and y >= 0 and self._board[y][x] is None

    def can_execute_operation(self, move, block):
        new_blocks = move.next_position(block)
        return self._iterate_condition(new_blocks)

    def clear_row(self, row_id):
        if None not in self._board[row_id]:
            self._board.pop(row_id)
            self._board.append([None for _ in range(self._width)])
            return True
        return False

    def clear_rows(self, rows):
        rows_cleared = 0

        # set reverse flag, so that poping rows doesn't interfere
        rows = sorted(rows, reverse=False)
        for row_id in rows:
            rows_cleared += self.clear_row(row_id)
        return rows_cleared
