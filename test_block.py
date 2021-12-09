from block import OBlock, TBlock, SBlock, IBlock


def test_o_block_turn():
    block = OBlock()
    position_start = block.get_blocks()
    block.turn_left()
    position_end = block.get_blocks()

    assert position_start == position_end


def test_t_block_turn():
    block = TBlock()
    block.turn_left()
    position = block.get_blocks()
    expected = ((-1, 0), (0, 0), (0, 1), (0, -1))

    assert sorted(position) == sorted(expected)


def test_s_block_opposite_turns():
    block = SBlock()
    position_start = block.get_blocks()
    block.turn_left()
    block.turn_right()
    position_end = block.get_blocks()

    assert sorted(position_start) == sorted(position_end)


def test_i_block_two_turns():
    block_1 = IBlock()
    block_1.turn_left()
    block_1.turn_left()

    block_2 = IBlock()
    block_2.turn_right()
    block_2.turn_right()

    position_1 = block_1.get_blocks()
    position_2 = block_2.get_blocks()
    expected = ((-2, -1), (-1, -1), (0, -1), (1, -1))

    assert position_1 == position_2 == expected


def test_s_block_four_turns():
    block = SBlock()
    position_start = block.get_blocks()
    block.turn_left()
    block.turn_left()
    block.turn_left()
    block.turn_left()
    position_end = block.get_blocks()

    assert sorted(position_start) == sorted(position_end)
