class ChessError(Exception):
    pass


class ColorError(ChessError):
    pass


class InvalidFEN(ChessError):
    pass


class InvalidMove(ChessError):
    pass


class InvalidNotation(ChessError):
    pass


class NotYourTurn(ChessError):
    pass