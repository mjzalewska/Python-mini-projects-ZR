class Player:
    def __init__(self, p_type):
        self.type = p_type
        self.pieces = []
        self.score = 0
        self.dames = 0

    def update_pieces_count(self):
        pass

    def update_score(self): # depends on other player's pieces count, if decrease - score increase
        pass

    def update_dames(self):
        pass


class Human(Player):
    def __init__(self):
        super().__init__()
        self.type = 'human'
        self.sign = 'P' #add num based on instance num


class Computer(Player):
    def __init__(self):
        super().__init__()
        self.type = 'computer'
        self.sign = 'C'
