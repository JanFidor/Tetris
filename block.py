# TESTED
from constants import Color


class Block:
    def __init__(self):
        self.color = Color.BLACK
        self._blocks = None

    def get_left_position(self):
        """
        Return blocks resulting from turning left
        """
        return tuple((-y, x) for x, y in self._blocks)

    def turn_left(self):
        """
        Set _blocks to blocks resulting from turning left
        """
        self._blocks = self.get_left_position()

    def get_right_position(self):
        """
        Return blocks resulting from turning right
        """
        return tuple((y, -x) for x, y in self._blocks)

    def turn_right(self):
        """
        Set _blocks to blocks resulting from turning right
        """
        self._blocks = self.get_right_position()

    def get_blocks(self):
        """
        Return _blocks
        """
        return self._blocks


class IBlock(Block):
    def __init__(self):
        self.color = Color.CYAN
        self._positions = (
            ((-2, 0), (-1, 0), (0, 0), (1, 0)),
            ((0, 1), (0, 0), (0, -1), (0, -2)),
            ((-2, -1), (-1, -1), (0, -1), (1, -1)),
            ((-1, 1), (-1, 0), (-1, -1), (-1, -2)),
        )
        self._position = 0

    def get_left_position(self):
        return self._positions[(self._position - 1) % len(self._positions)]

    def get_right_position(self):
        return self._positions[(self._position + 1) % len(self._positions)]

    def turn_left(self):
        self._position = (self._position - 1) % len(self._positions)
        return self._positions[self._position]

    def turn_right(self):
        self._position = (self._position + 1) % len(self._positions)
        return self._positions[self._position]

    def get_blocks(self):
        return self._positions[self._position]


class JBlock(Block):
    def __init__(self):
        self.color = Color.DARK_BLUE
        self._blocks = ((-1, 1), (-1, 0), (0, 0), (1, 0))


class LBlock(Block):
    def __init__(self):
        self.color = Color.ORANGE
        self._blocks = ((-1, 0), (0, 0), (1, 0), (1, 1))


class OBlock(Block):
    def __init__(self):
        self.color = Color.YELLOW
        self._blocks = ((0, 0), (0, 1), (1, 0), (1, 1))

    def get_left_position(self):
        return self._blocks

    def get_right_position(self):
        return self._blocks


class SBlock(Block):
    def __init__(self):
        self.color = Color.GREEN
        self._blocks = ((-1, 0), (0, 0), (0, 1), (1, 1))


class TBlock(Block):
    def __init__(self):
        self.color = Color.PURPLE
        self._blocks = ((-1, 0), (0, 0), (1, 0), (0, 1))


class ZBlock(Block):
    def __init__(self):
        self.color = Color.RED
        self._blocks = ((-1, 1), (0, 1), (0, 0), (1, 0))
