from Checkers.utilities.utilities import convert


class Player:
    player_count = 0

    def __init__(self, p_type, name):
        self.type = p_type
        self.__class__.player_count += 1
        self.color = None
        self.name = name
        self.pieces = []
        self.score = 0
        self.kings = 0

    def set_player_color(self, color):
        self.color = color

    def update_pieces_count(self):
        pass

    def update_kings_count(self):
        pass

    def get_mandatory_captures(self, board):
        mandatory_captures = []
        for piece in self.pieces:
            if piece.rank == 'pawn':
                if piece.color == 'white':
                    dirs = [[2, -2], [2, 2]]
                else:
                    dirs = [[-2, -2], [-2, 2]]
            else:
                dirs = [[2, -2], [2, 2], [-2, -2], [-2, 2]]

            for d in dirs:
                target_field = (piece.position[0] + d[0], piece.position[1] + d[1])
                if piece.is_move_allowed(board, target_field, self, piece.color):
                    mandatory_captures.append((convert(index=piece.position), convert(index=target_field)))
        return mandatory_captures

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
