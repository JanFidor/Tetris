# SEEMS VAGUELY DONE, MIGHT NEED ARCHTECTURAL CHANGES LATER


# center of board, at the top of visible board (with enough place for)
BOARD_W = 10
BOARD_H = 24
STARTING_LOCATION = (BOARD_W // 2, BOARD_H - 2)


class BlockFalling:
    def __init__(self, block):
        self._location = list(STARTING_LOCATION)
        self._block = block

    def get_location(self):
        return tuple(self._location)

    def go_left(self):
        self._location[0] -= 1

    def go_right(self):
        self._location[0] += 1

    def go_down(self):
        self._location[1] -= 1

    def turn_left(self):
        self._block.turn_left()

    def turn_right(self):
        self._block.turn_right()

    def blocks_on_board(self):
        x1, y1 = self._location
        return tuple((x1 + x2, y1 + y2) for x2, y2 in self._block._blocks)

    def color(self):
        return self._block.color
