
class TetrisManager:
    def __init__(self):
        self._score = 0
        self._time = 0
        self._level = 0

    def add_points(self, points):
        self._score += points
