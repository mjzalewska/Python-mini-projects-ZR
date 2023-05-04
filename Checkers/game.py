from art import tprint
from classes.piece import Piece
from classes.player import Player
from classes.board import Board


class Game:
    game_state = 'initializing'
    board = None

    @classmethod
    def show_welcome_screen(cls):
        tprint('Checkers', font='tarty1')  # tarty9
        print()
        print('Welcome to the game of Python Checkers! Let\'s start!\n')

    @classmethod
    def choose_game_mode(cls):
        modes = ['1', '2']
        print('Please choose your game mode')
        print('1 - Player vs Player')
        print('2 - Player vs Computer')
        while True:
            mode_choice = input()
            try:
                if mode_choice in modes:
                    return mode_choice
                else:
                    raise IndexError
            except IndexError:
                print('Incorrect input. Please choose 1 or 2')

    @classmethod
    def take_coordinates(cls):  # osobno target i source? # define in pawn.move
        print("Which pawn would you like to move? Please name the source and target fields")
        while True:
            source_field = input("Move from: ")
            target_field = input("Move to: ")
            try:
                if source_field.upper() and target_field.upper() in Board.p_fields.keys():
                    return source_field, target_field
                else:
                    raise KeyError
            except KeyError:
                print("Incorrect input. Either the source or target field number is incorrect. Please try again")

    @classmethod
    def initialize(cls):
        # initialize players
        if Game.choose_game_mode() == '1':
            player_1 = Player('human')
            player_2 = Player('human')
        else:
            player_1 = Player('human')
            player_2 = Player('computer')

        # initialize game board
        cls.board = Board()

        # initialize pawns
        for num in range(1, 13):
            piece_w = Piece('white')
            piece_w.set_name('w')
            player_1.pieces.append(piece_w)
            piece_b = Piece('black')
            piece_b.set_name('b')
            player_2.pieces.append(piece_b)

        # assign pieces to initial positions on board
        for i in range(len(list(Board.p_fields.keys())[:12])):
            Board.p_fields[list(Board.p_fields.keys())[i]] = player_1.pieces[i]
        for j in range(len(list(Board.p_fields.keys())[20:])):
            Board.p_fields[list(Board.p_fields.keys())[j + 20]] = player_2.pieces[j]

        # assign  initial board position to pieces
        for piece in player_1.pieces:
            for key in Board.p_fields.keys():
                if Board.p_fields[key] == piece:
                    piece.set_initial_position(key)

        for piece in player_2.pieces:
            for key in Board.p_fields.keys():
                if Board.p_fields[key] == piece:
                    piece.set_initial_position(key)

        cls.game_state = 'playing'

    @classmethod
    def play(cls):
        pass


# manual test code
# Game.choose_game_mode()
Game.initialize()
# Board.display_board(Board.p_fields)

