
class Strategy:
    def _operation(block):
        pass

    @classmethod
    def next_position(cls, block):
        loc_x, loc_y = block.location
        blocks = cls._operation(block)
        return tuple((x + loc_x, y + loc_y) for x, y in blocks)

    def set_position(block):
        pass


class GoLeft(Strategy):
    def _operation(block):
        return tuple((x - 1, y) for x, y in block.get_blocks())

    def set_position(block):
        x, y = block.location
        block.location = x - 1, y


class GoRight(Strategy):
    def _operation(block):
        return tuple((x + 1, y) for x, y in block.get_blocks())

    def set_position(block):
        x, y = block.location
        block.location = x + 1, y


class GoDown(Strategy):
    def _operation(block):
        return tuple((x, y - 1) for x, y in block.get_blocks())

    def set_position(block):
        x, y = block.location
        block.location = x, y - 1


class TurnLeft(Strategy):
    def _operation(block):
        return block.get_inner_block().get_left_position()

    def set_position(block):
        block.get_inner_block().turn_left()


class TurnRight(Strategy):
    def _operation(block):
        return block.get_inner_block().get_right_position()

    def set_position(block):
        block.get_inner_block().turn_right()
