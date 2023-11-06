from colorama import Fore
from math import ceil
from Checkers.classes.board import Board
from Checkers.utilities.utilities import convert


# just_fix_windows_console()

class Piece:
    def __init__(self, color):
        self.color = color
        self.position = None
        self.name = None
        self.rank = None
        self.status = 'active'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def set_initial_position(self, position: tuple):
        self.position = position

    def move(self, new_position: tuple):
        old_line, old_column = self.position
        new_line, new_col = new_position
        Board.fields[old_line][old_column] = ' '
        Board.fields[new_line][new_col] = self
        self.position = new_position

    def remove_piece(self, new_status, player):
        self.status = new_status
        player.pieces.remove(self)
        line, column = self.position
        Board.fields[line][column] = ' '


    def is_own_piece(self, player):
        if self in player.pieces:
            return True
        return False


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.name = '\u23FA'
        else:
            self.name = '\U0001F785'
        self.rank = 'pawn'

    def is_move_allowed(self, board, new_position: str, player, turn):
        old_line, old_column = self.position
        new_line, new_column = convert(field=new_position)
        mid_line, mid_column = ceil((old_line + new_line) / 2), ceil((old_column + new_column) / 2)
        other_piece = board.fields[mid_line][mid_column]
        if 0 <= new_line <= 7 and 0 <= new_column <= 7:
            if turn == 'white':
                if new_line - old_line == 1 and new_column - old_column in [-1, 1] and \
                        board.fields[new_line][new_column] == ' ':
                    return True
                elif new_line - old_line == 2 and new_column - old_column in [-2, 2] and \
                        board.fields[mid_line][mid_column] != ' ' and not other_piece.is_own_piece(player) and \
                        board.fields[new_line][new_column] == ' ':
                    return True
                return False
            else:
                if new_line - old_line == -1 and new_column - old_column in [-1, 1] and \
                        board.fields[new_line][new_column] == ' ':
                    return True
                elif new_line - old_line == -2 and new_column - old_column in [-2, 2] and \
                        board.fields[mid_line][mid_column] != ' ' and not other_piece.is_own_piece(player) and \
                        board.fields[new_line][new_column] == ' ':
                    return True
                return False
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


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        if self.color == 'white':
            self.name = '\u265A'
        else:
            self.name = '\u2654'
        self.rank = 'king'

    def __str__(self):
        if self.color == 'white':
            return str(Fore.RED + self.name)
        else:
            return str(Fore.BLUE + self.name)

    def is_move_allowed(self, board, new_position):
        old_line, old_column = self.position
        new_line, new_column = new_position
        mid_line, mid_column = old_line + new_line // 2, old_column + new_column // 2
        other_piece = board.fields[mid_line][mid_column]
        if abs(new_line - old_line) == 1 and abs(new_column - old_column) == 1 and \
                board.fields[new_line][new_column] == ' ':
            return True
        elif abs(new_line - old_line) == 2 and abs(new_column - old_column) == 2 and \
                board[mid_line][mid_column] != ' ' and not other_piece.is_own_piece() and \
                board.fields[new_line][new_column] == ' ':
            return True
        else:
            return False
