from classes.piece import Piece
from classes.player import Player
from classes.board import Board


class Game:
    game_state = 'initializing'
    board = None

    @classmethod
    def initialize(cls):
        player_1 = Player('human')
        player_2 = Player('human')

        cls.board = Board()

        for num in range(1, 25):
            if num <= 12:
                piece = Piece('white')
                piece.name = 'w' + str(num)
                # assign position on board and assign to board
                player_1.pieces.append(piece)

            else:
                piece = Piece('black')
                piece.name = 'b' + str(num)
                # assign position on board and assign  to board
                player_2.pieces.append(piece)

        for key in Board.p_fields.keys():
            if key[0] in ['A', 'B', 'C']:
                pass
            elif key[0] in ['F', 'G', 'H']:
                pass

        print(player_1.pieces)
        print(len(player_1.pieces))


Game.initialize()
