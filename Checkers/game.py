from art import tprint
from classes.piece import Piece
from classes.player import Player
from classes.board import Board


class Game:
    game_state = 'initializing'
    board = None

    @classmethod
    def show_welcome_screen(cls):
        tprint('Checkers', font='tarty1') # tarty9
        print()
        print('Welcome to the game of Python Checkers! Let\'s start!')

    @classmethod
    def show_menu(cls):
        pass

    @classmethod
    def choose_game_mode(cls):
        print('Please choose your game mode')
        print('1 - Player vs Player')
        print('2 - Player vs Computer')
        while True:
            pass

    @classmethod
    def take_input(cls):
        pass

    @classmethod
    def initialize(cls):
        # initialize players
        player_1 = Player('human')
        player_2 = Player('human') # change to reflect player's choice (vs comp or vs human)

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
            # change board display func

        # assign pieces to initial positions on board
        for i in range(len(list(Board.p_fields.keys())[:12])):
            Board.p_fields[list(Board.p_fields.keys())[i]] = player_1.pieces[i]
        for j in range(len(list(Board.p_fields.keys())[20:])):
            Board.p_fields[list(Board.p_fields.keys())[j+20]] = player_2.pieces[j]

        cls.game_state = 'playing'

    @classmethod
    def play(cls):
        pass

Game.show_welcome_screen()
