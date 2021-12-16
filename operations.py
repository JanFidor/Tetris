
class Operation:
    def _new_blocks_positions(block):
        pass

    @classmethod
    def next_position(cls, block):
        loc_x, loc_y = block.location
        blocks = cls._new_blocks_positions(block)
        return tuple((x + loc_x, y + loc_y) for x, y in blocks)

    def change_position(block):
        pass


class GoLeft(Operation):
    def _new_blocks_positions(block):
        return tuple((x - 1, y) for x, y in block.get_blocks())

    def change_position(block):
        x, y = block.location
        block.location = x - 1, y


class GoRight(Operation):
    def _new_blocks_positions(block):
        return tuple((x + 1, y) for x, y in block.get_blocks())

    def change_position(block):
        x, y = block.location
        block.location = x + 1, y


class GoDown(Operation):
    def _new_blocks_positions(block):
        return tuple((x, y - 1) for x, y in block.get_blocks())

    def change_position(block):
        x, y = block.location
        block.location = x, y - 1


class TurnLeft(Operation):
    def _new_blocks_positions(block):
        return block.get_inner_block().get_left_position()

    def change_position(block):
        block.get_inner_block().turn_left()


class TurnRight(Operation):
    def _new_blocks_positions(block):
        return block.get_inner_block().get_right_position()

    def change_position(block):
        block.get_inner_block().turn_right()
