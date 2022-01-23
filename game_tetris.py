from board import Board
from generator import generate_random_block
from operations import GoDown
from block_falling import BlockFalling


class Tetris:
    def __init__(self, difficulty=1):
        self._difficulty = difficulty

        self._board = Board()
        self._block = None

        self._points = 0
        self._running = True

        self.generate_random_block()

    def generate_random_block(self):
        """
        Generate random block and create Falling Block with it and save as
        _block
        """
        random_block = generate_random_block()
        width, height = self._board.dimensions()
        self._block = BlockFalling(random_block, width, height)

    def land_block(self):
        """
        Land block saved in _block on the board, end game or generate a new one
        """

        if self._board.is_above_board(self._block):
            self.game_over()
            # placing return here disrupts self.drop_block()

        self._board.land_block(self._block)
        self.clear_rows(self._block.blocks_on_board())

        self.generate_random_block()

    def clear_rows(self, blocks):
        """
        Clear empty rows of the board and add appropriate amount of points
        to score

        Keyword arguments: blocks -> blocks consisting of current _block
        """
        def filter_out_unique_row_ids(blocks):
            return set([y for _, y in blocks])

        row_ids = filter_out_unique_row_ids(blocks)
        cleared_rows = self._board.clear_rows(row_ids)

        self.calculate_and_add_points_earned(cleared_rows)

    def calculate_and_add_points_earned(self, cleared_rows):
        """
        Calculate amount of points earned from clearing 'cleared_rows' rows
        and add them to score

        Keyword arguments: cleared_rows - amount of rows cleared
        """
        multiplier = self._difficulty
        width = self._board._width
        points = cleared_rows * width * multiplier

        self._points += points

    def game_over(self):
        self._running = False

    def get_board(self):
        return self._board

    def is_running(self):
        return self._running

    def execute_operation(self, operation):
        """
        Execute operation 'operation' on _block

        Keyword arguments: operation -> passed operation of type 'operation'
        """
        self._board.clear_block(self._block)

        if self._board.can_execute_operation(operation, self._block):
            self._block.execute_operation(operation)

        if not self._board.can_execute_operation(GoDown, self._block):
            self.land_block()

        self._board.place_block(self._block)

    def drop_block(self):
        """
        Execute operation 'GoDown' on _block until it lands
        """
        block = self._block
        while self._block == block:
            self.execute_operation(GoDown)
