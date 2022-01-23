from block_falling import BlockFalling
from game_tetris import Tetris
from board import Board


def test_contructor():
    tetris = Tetris()
    board = tetris._board
    block = tetris._block
    assert isinstance(block, BlockFalling) and isinstance(board, Board)


def test_drop_block():
    tetris = Tetris()
    tetris.drop_block()
    bottom_row = tetris._board._board[0]
    bottom_row_filtered = [block for block in bottom_row if block is not None]
    assert len(bottom_row_filtered) != 0
