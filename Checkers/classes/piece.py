from Checkers.classes.board import Board
from Checkers.classes.player import Player
from Checkers.utilities.utilities import convert


class Piece:
    def __init__(self):
        self.color = None
        self.position = None
        self.name = None
        self.rank = None
        self.status = 'active'

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def set_initial_position(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position
        new_position_index = convert(field=self.position)
        print(new_position_index)
        new_line, new_col = new_position_index
        Board.board_fields[new_line + 1][new_col + 1] = self

    def remove_from_gameplay(self, new_status, player):
        self.status = new_status
        player.pieces.remove(self)
        player.update_pieces_count()

    def set_movement_type(self):
        pass

    @staticmethod
    def is_opponent_piece(other_piece, player):
        if other_piece in player.pieces:
            return True
        return False

    def can_capture_multiple(self):
        pass


class Pawn(Piece):
    def __init__(self):
        super().__init__()


class WhitePawn(Pawn):
    def __init__(self):
        super().__init__()
        self.name = '\u23FA'
        self.rank = 'pawn'


class BlackPawn(Pawn):
    def __init__(self):
        super().__init__()
        self.name = '\U0001F785'
        self.rank = 'pawn'


class King(Piece):
    def __init__(self):
        super().__init__()


class WhiteKing(King):
    def __init__(self):
        super().__init__()
        self.name = '\u265A'
        self.rank = 'king'


class BlackKing(King):
    def __init__(self):
        super().__init__()
        self.name = '\u2654'
        self.rank = 'king'







