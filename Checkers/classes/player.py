class Player:
    def __init__(self):
        self.type = None
        self.sign = None
        self.pieces = 12
        self.score = 0
        self.dames = 0

    def update_pieces_count(self):
        pass

    def update_score(self):
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
