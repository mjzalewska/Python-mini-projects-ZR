from Checkers.utilities.utilities import convert


class Player:
    player_count = 0

    def __init__(self, p_type, name, side):
        self.type = p_type
        self.__class__.player_count += 1
        self.color = None
        self.name = name
        self.side = side
        self.pieces = []
        self.score = 0

    def set_player_color(self, color):
        self.color = color

    def get_mandatory_captures(self, board):
        mandatory_captures = []
        for piece in self.pieces:
            if piece.rank == 'pawn':
                if self.side == 'top':
                    dirs = [[2, -2], [2, 2]]
                else:
                    dirs = [[-2, -2], [-2, 2]]
            else:
                dirs = [[2, -2], [2, 2], [-2, -2], [-2, 2]]

            for d in dirs:
                target_line, target_column = (piece.position[0] + d[0], piece.position[1] + d[1])
                if target_line in range(8) and target_column in range(8):
                    target_field = convert(index=(target_line, target_column))
                    if piece.is_move_allowed(board, target_field, self):
                        mandatory_captures.append((convert(index=piece.position), target_field))
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
                    if self.side == "top":
                        dirs = [[1, -1], [1, 1], [2, -2], [2, 2]]
                    else:
                        dirs = [[-1, -1], [-1, 1], [-2, -2], [-2, 2]]
                    for d in dirs:
                        if piece.is_move_allowed(board, convert(index=(line + d[0], column + d[1])), self):
                            result.append(1)
                        result.append(0)
                else:
                    dirs = [[-1, -1], [-1, 1], [1, -1], [1, 1], [2, -2], [2, 2],[-2, -2], [-2, 2]]
                    for d in dirs:
                        if piece.is_move_allowed(board, convert(index=(line + d[0], column + d[1])), self):
                            result.append(1)
                        result.append(0)
            return any(result)

    def update_score(self):
        self.score += 1

