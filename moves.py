class Move:
    def _operation(self, block):
        pass


class GoLeft(Move):
    def _operation(block):
        return tuple((x - 1, y) for x, y in block.blocks_on_board())


class GoRight(Move):
    def _operation(block):
        return tuple((x + 1, y) for x, y in block.blocks_on_board())


class GoDown(Move):
    def _operation(block):
        return tuple((x, y - 1) for x, y in block.blocks_on_board())


class TurnLeft(Move):
    def _operation(block):
        return block._block.get_left_position()


class TurnRight(Move):
    def _operation(block):
        return block.get_right_position()
