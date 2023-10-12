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
        new_line, new_col = new_position
        Board.board_fields[new_line][new_col] = self

    def remove(self, new_status, player):
        self.status = new_status
        player.pieces.remove(self)
        player.update_pieces_count()

    def is_own_piece(self, player):
        if self in player.pieces:
            return True
        return False


class Pawn(Piece):

    def __init__(self):
        super().__init__()

    def is_move_allowed(self, board, other_piece, new_position):
        old_line, old_column = self.position
        new_line, new_column = new_position
        mid_line, mid_column = old_line + new_line / 2, old_column + new_column / 2
        if new_line - old_line == 1 and new_column - old_column in [-1, 1] and \
                board.board_fields[new_line][new_column] == ' ':
            return True
        elif new_line - old_line == 2 and new_column - old_column in [-2, 2] and \
                board[mid_line][mid_column] != ' ' and not other_piece.is_own_piece() and \
                board.board_fields[new_line][new_column] == ' ':
            return True
        else:
            return False

    def is_promoted(self):
        if self.color == 'white' and self in Board.black_promotion_line:
            return True
        elif self.color == 'black' and self in Board.white_promotion_line:
            return True
        return False

    def promote_pawn(self):
        if self.is_promoted():
            self.rank = 'king'


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

    def is_move_allowed(self, board, other_piece, new_position):
        old_line, old_column = self.position
        new_line, new_column = new_position
        mid_line, mid_column = old_line + new_line / 2, old_column + new_column / 2
        if abs(new_line - old_line) == 1 and abs(new_column - old_column) == 1 and \
                board.board_fields[new_line][new_column] == ' ':
            return True
        elif abs(new_line - old_line) == 2 and abs(new_column - old_column) == 2 and \
                board[mid_line][mid_column] != ' ' and not other_piece.is_own_piece() and \
                board.board_fields[new_line][new_column] == ' ':
            return True
        else:
            return False


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
