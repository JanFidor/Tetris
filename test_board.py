from board import Board
from block_falling import BlockFalling
from block import TBlock, IBlock


def test_board_can_not_go_left():
    block = TBlock()
    block_falling = BlockFalling(block)
    board = Board()

    block_falling.go_left()
    block_falling.go_left()
    block_falling.go_left()
    block_falling.go_left()

    assert not board.can_go_left(block_falling)


def test_board_can_go_left():
    block = TBlock()
    block_falling = BlockFalling(block)
    board = Board()

    block_falling.go_right()

    assert board.can_go_left(block_falling)


def test_board_can_not_go_down():
    block = TBlock()
    block_falling = BlockFalling(block)
    board = Board()

    while block_falling.get_location()[1] > 0:
        block_falling.go_down()

    assert not board.can_go_down(block_falling)


def test_board_can_not_turn_left():
    block = IBlock()
    block_falling = BlockFalling(block)
    board = Board()

    block_falling.turn_right()
    block_falling.go_left()
    block_falling.go_left()
    block_falling.go_left()
    block_falling.go_left()

    assert not board.can_turn_left(block_falling)
