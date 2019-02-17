from chess import Chess


class Singleton:
    _chess = None

    def __init__(self):
        self.chess = Chess

    @property
    def chess(self):
        print(type(self._chess))
        return self._chess

    @chess.setter
    def chess(self, cls):
        if self._chess is None:
            self._chess = cls()
