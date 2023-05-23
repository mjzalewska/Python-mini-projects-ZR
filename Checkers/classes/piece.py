from .board import Board
from .player import Player


class Piece:
    def __init__(self, color):
        self.color = color
        self.position = None
        self.name = None
        self.rank = 'pawn'
        self.status = 'active'

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def set_initial_position(self, position):
        self.position = position

    def move(self, new_position):
        self.position = new_position
        Board.p_fields[new_position] = self

    def remove_from_gameplay(self, new_status, player):
        self.status = new_status
        player.pieces.remove(self)
        player.update_pieces_count()

    def set_new_rank(self, new_rank):
        self.rank = new_rank

    def set_movement_type(self):
        pass

    @staticmethod
    def is_opponent_piece(other_piece, player):
        if other_piece in player.pieces:
            return True
        return False

    def can_capture_multiple(self):
        pass



