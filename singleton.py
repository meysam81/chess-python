from chess import Chess


class Singleton:
    _chess = None

    @property
    def chess(self):
        if Singleton._chess is None:
            Singleton._chess = Chess()
        return Singleton._chess

    @chess.setter
    def chess(self, item):
        raise Exception("You cannot re-assign a singleton object!")
