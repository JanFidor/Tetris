from board import Board
from generator import generate_random_block
from difficulties import Difficulty
from tetris_manager import TetrisManager


class Tetris:
    def ___init__(self, difficulty: Difficulty):
        self._difficulty = difficulty
        # use inside
        self._tetris_manager = TetrisManager()
        self._board = Board()
        self._block = None

        self.generate_random_block()

    def generate_random_block(self):
        self._block = generate_random_block()

    def land_block(self):
        if self._board.is_above_board(self._block):
            self.game_over()

        blocks = self._block.blocks_on_board()
        for x, y in blocks:
            # board.land_block()!!
            self._board[y][x] = self._block.color()

        self.clear_rows(blocks)

        # self._block = None
        self.generate_random_block()

    def clear_rows(self, blocks):
        def filter_out_unique_row_ids(blocks):
            return set([y for x, y in blocks])

        row_ids = filter_out_unique_row_ids(blocks)
        cleared_rows = self._board.clear_rows(row_ids)

        multiplier = self._difficulty.get_multiplier()
        width = self._board._width
        points = cleared_rows * width * multiplier

        self._tetris_manager.add_points(points)

    def game_over(self):
        pass

    def execute_operation(self, operation):
        if self._board.can_execute_operation(operation, self._block):
            self._block.execute_operation(operation)

        if self._board.land_block(self._block):
            self.land_block()
