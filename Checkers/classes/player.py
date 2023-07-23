class Player:
    def __init__(self, p_type):
        self.type = p_type
        self.pieces = []
        self.score = 0
        self.kings = 0

    def update_pieces_count(self):
        pass

    def update_score(self):  # depends on other player's pieces count, if decrease - score increase
        pass

    def update_kings(self):
        pass

