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

    def move(self):
        pass
        # if moving only - +1, if moving and capturing +2
        # needs to 'know' if another piece in its way

    def set_status(self):
        pass

    def set_position(self):
        pass

    def set_rank(self):
        pass

    def set_movement(self):
        pass

    def set_symbol(self):
        pass
