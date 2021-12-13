from block import OBlock, SBlock
from block_falling import BlockFalling, BOARD_H, BOARD_W
from operations import GoDown, GoLeft, GoRight, TurnLeft


def test_block_falling_starting_location():
    block = OBlock()
    block_falling = BlockFalling(block)

    assert block_falling.location == (BOARD_W // 2, BOARD_H + 2)


def test_block_falling_change_location():
    block = OBlock()
    block_falling = BlockFalling(block)

    # move by vector (-1, -2)
    block_falling.execute_operation(GoDown)
    block_falling.execute_operation(GoDown)
    block_falling.execute_operation(GoLeft)
    block_falling.execute_operation(GoLeft)
    block_falling.execute_operation(GoRight)
    block_falling.execute_operation(TurnLeft)

    expected = (BOARD_W // 2 - 1, BOARD_H - 2 + 2)

    assert block_falling.location == expected


def test_block_falling_blocks_on_board():
    block = SBlock()
    block_falling = BlockFalling(block)

    # move by vector (-1, -2) and turn 90*
    block_falling.execute_operation(GoDown)
    block_falling.execute_operation(GoDown)
    block_falling.execute_operation(GoLeft)
    block_falling.execute_operation(TurnLeft)

    expected = sorted(((3, 21), (3, 20), (4, 20), (4, 19)))
    gotten = sorted(block_falling.blocks_on_board())

    assert gotten == expected
