from Checkers.utilities.utilities import convert


class Player:
    def __init__(self, p_type, color):
        self.type = p_type
        self.color = color
        self.pieces = []
        self.score = 0
        self.kings = 0

    def update_pieces_count(self):
        pass

    def update_kings_count(self):
        pass

    def has_piece_left(self):
        if self.pieces:
            return True
        return False

    def has_moves_left(self, board):
        if self.has_piece_left():
            result = []
            for piece in self.pieces:
                line, column = piece.position
                if piece.rank == "pawn":
                    if piece.color == "white":
                        dirs = [[1, -1], [1, 1], [2, -2], [2, 2]]
                    else:
                        dirs = [[-1, -1], [-1, 1], [-2, -2], [-2, 2]]
                else:
                    dirs = [[-1, -1], [-1, 1], [1, -1], [1, 1], [2, -2], [2, 2],[-2, -2], [-2, 2]]

                for d in dirs:
                    if piece.is_move_allowed(board, (line + d[0], column + d[1]), self, self.color):
                        result.append(1)
                    result.append(0)
            return any(result)
