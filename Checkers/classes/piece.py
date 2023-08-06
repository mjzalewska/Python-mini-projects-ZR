from Checkers.classes.board import Board
from Checkers.utilities.utilities import convert
from colorama import Fore


# just_fix_windows_console()

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
        new_line, new_col = new_position_index
        Board.board_fields[new_line][new_col] = self

    def remove_from_gameplay(self, new_status, player):
        self.status = new_status
        player.pieces.remove(self)
        player.update_pieces_count()

    @staticmethod
    def is_own_piece(piece_location, player, board):
        field_line, field_col = convert(field=piece_location)
        if board[field_line][field_col] in player.pieces:
            return True
        return False


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

    def __repr__(self):
        return str(Fore.RED + self.name)

    def __str__(self):
        return str(Fore.RED + self.name)


class BlackKing(King):
    def __init__(self):
        super().__init__()
        self.name = '\u2654'
        self.rank = 'king'

    def __repr__(self):
        return str(Fore.BLUE + self.name)

    def __str__(self):
        return str(Fore.BLUE + self.name)
