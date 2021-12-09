from board import Board
from generator import generate_random_block


class Tetris:
    def ___init__(self):
        self.tetris = None
        self._board = Board()
        self._block = None

        self.generate_random_block()
    
    def get_tetris():
        if self.tetris = None:

    def generate_random_block(self):
        self._block = generate_random_block()

    def block_landed(self):
        if self._board.is_above_board(self._block):
            self.game_over()

        blocks = self._block.blocks_on_board()
        for x, y in blocks:
            self._board[y][x] = self._block.color()
        self._block = None

    def game_over(self):
        pass

    def go_left(self):
        if self._board.can_go_left(self._block):
            self._block.go_left()

        if self._board.block_landed(self._block):
            self.block_landed()

    def go_right(self):
        if self._board.can_go_right(self._block):
            self._block.go_right()

        if self._board.block_landed(self._block):
            self.block_landed()

    def go_down(self):
        if self._board.can_go_down(self._block):
            self._block.go_down()

        if self._board.block_landed(self._block):
            self.block_landed()

    def turn_left(self):
        if self._board.can_turn_left(self._block):
            self._block.turn_left()

        if self._board.block_landed(self._block):
            self.block_landed()

    def turn_right(self):
        if self._board.can_turn_right(self._block):
            self._block.turn_right()

        if self._board.block_landed(self._block):
            self.block_landed()
