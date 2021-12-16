from board import Board
from block_falling import BlockFalling
from block import TBlock, IBlock, OBlock
from operations import GoLeft, GoDown, TurnLeft, TurnRight


def test_board_can_not_go_left():
    block = TBlock()
    block_falling = BlockFalling(block)
    board = Board()

    for i in range(4):
        block_falling.execute_operation(GoLeft)

    assert not board.can_execute_operation(GoLeft, block_falling)


def test_board_can_go_left():
    block = TBlock()
    block_falling = BlockFalling(block)
    board = Board()

    block_falling.execute_operation(GoLeft)

    assert board.can_execute_operation(GoLeft, block_falling)


def test_board_can_not_go_down():
    block = TBlock()
    block_falling = BlockFalling(block)
    board = Board()

    while block_falling.location[1] > 0:
        block_falling.execute_operation(GoDown)

    assert not board.can_execute_operation(GoDown, block_falling)


def test_board_can_not_turn_left():
    block = IBlock()
    block_falling = BlockFalling(block)
    board = Board()

    block_falling.execute_operation(TurnRight)
    for i in range(4):
        block_falling.execute_operation(GoLeft)

    assert not board.can_execute_operation(TurnLeft, block_falling)


def test_is_above_board():
    block = IBlock()
    block_falling = BlockFalling(block)
    board = Board()

    assert board.is_above_board(block_falling)


def test_land_block():
    block = OBlock()
    block_falling = BlockFalling(block)
    board = Board()

    while board.can_execute_operation(GoDown, block_falling):
        block_falling.execute_operation(GoDown)

    board.land_block(block_falling)

    block_positions = block_falling.blocks_on_board()
    board_values = [board._board[y][x] for x, y in block_positions]

    assert None not in board_values


def test_clear_rows():
    board = Board()

    width = len(board._board[0])

    board._board[0] = [1 for i in range(width)]
    board._board[1] = [1 for i in range(width)]
    board._board[2][0] = 2

    cleared = board.clear_rows((0, 1, 2, 3))

    check_1 = cleared == 2
    check_2 = board._board[0][0] == 2
    check_3 = board._height == len(board._board) - 4

    assert check_1 and check_2 and check_3
