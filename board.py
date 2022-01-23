from operations import OperationStrategy
from constants import BOARD_W, BOARD_H, MAX_BLOCK_HEIGHT


class BlockIsNullError(Exception):
    def __init__(self):
        super().__init__("Block not added to BlockFallingManager")


class Board:
    def generate_empty_row(self):
        """
        Generate empty row for Tetris board and return it
        """
        return [None for _ in range(self._width)]

    def __init__(self):
        self._width = BOARD_W
        self._height = BOARD_H

        board_height = self._height + MAX_BLOCK_HEIGHT
        self._board = [self.generate_empty_row() for _ in range(board_height)]

    def get_block(self, x, y):
        """
        Return blocks color or None at x, y at _board

        Keyword arguments: x -> x position
        Keyword arguments: y -> y position
        """
        return self._board[y][x]

    def place_block(self, block_falling):
        """
        Save color of block_falling inside _board at appropriate coordinates
        """
        for block in block_falling.blocks_on_board():
            x, y = block
            self._board[y][x] = block_falling.get_color()

    def clear_block(self, block_falling):
        """
        Clear blocks of block_falling from the _board
        """
        for block in block_falling.blocks_on_board():
            x, y = block
            self._board[y][x] = None

    def _verify_block_not_null(block):
        if block is None:
            raise BlockIsNullError()

    def land_block(self, block_falling):
        """
        Save color of block_falling positions of its blocks
        """
        Board._verify_block_not_null(block_falling)

        for x, y in block_falling.blocks_on_board():
            self._board[y][x] = block_falling.get_color()

    def is_above_board(self, block_falling):
        """
        Check if block_falling has a block above the board
        """
        Board._verify_block_not_null(block_falling)

        for _, y in block_falling.blocks_on_board():
            if y >= self._height:
                return True
        return False

    def _iterate_condition(self, positions: tuple):
        """
        Check if _existance_condition is met for all positions of 'positions'
        Returned: boolean
        """
        blocks_checks = []
        for block_x, block_y in positions:
            blocks_checks.append(self._existance_condition(block_x, block_y))

        return all(blocks_checks)

    def _existance_condition(self, x: int, y: int):
        """
        Check if block can exist at those coordinates

        Keyword arguments: x -> x position
        Keyword arguments: y -> y position

        Returned: boolean
        """
        if not 0 <= x < BOARD_W:
            return False
        if y < 0:
            return False
        if self._board[y][x] is not None:
            return False
        return True

    def can_execute_operation(self, operation: OperationStrategy, block_falling):
        """
        Check if after executing the operation block_falling could exist on
        board
        """
        Board._verify_block_not_null(block_falling)
        new_blocks = operation.next_position(block_falling)
        can_execute = self._iterate_condition(new_blocks)

        return can_execute

    def clear_row(self, row_id: int) -> bool:
        """
        Check if can empty the row, return the result and empty the row if
        possible
        """
        if None not in self._board[row_id]:
            self._board.pop(row_id)
            self._board.append([None for _ in range(self._width)])
            return True
        return False

    def clear_rows(self, rows: set):
        """
        Clear rows that can be cleared, return how many were
        """
        rows_cleared = 0

        # set reverse flag, so that poping rows doesn't interfere
        rows = sorted(rows, reverse=True)
        for row_id in rows:
            if self.clear_row(row_id):
                rows_cleared += 1
        return rows_cleared

    def dimensions(self):
        return self._width, self._height
