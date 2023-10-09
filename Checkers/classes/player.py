class Player:
    def __init__(self, p_type):
        self.type = p_type
        self.pieces = []
        self.score = 0
        self.kings = 0

    def update_pieces_count(self):
        pass

    def update_kings_count(self):
        self.kings += 1

    def is_piece_left(self):
        if len(self.pieces) > 0:
            return True
        return False

    def is_movement_left(self):
        pass

