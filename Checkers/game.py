from art import tprint
from classes.piece import Piece
from classes.player import Player
from classes.board import Board
from Checkers.utilities.utilities import convert


class Game:
    game_state = 'initializing'
    board = None
    player_1 = None
    player_2 = None

    # TODO: add rules ?
    @classmethod
    def show_welcome_screen(cls):
        tprint('Checkers', font='tarty1')  # tarty9
        print()
        print('Welcome to the game of Python Checkers! Let\'s start!\n')

    @classmethod
    def game_over(cls):
        tprint('Game over', font='tarty1')

    @classmethod
    def choose_game_mode(cls):
        modes = ['1', '2']
        print('Please choose how you want to play: ')
        print('1 - Player vs Player')
        print('2 - Player vs Computer')
        while True:
            mode_choice = input()
            try:
                if mode_choice in modes:
                    return mode_choice
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect input. Please choose 1 or 2')

    @classmethod
    def initialize(cls):
        # initialize players
        match Game.choose_game_mode():
            case '1':
                cls.player_1 = Player('human')
                cls.player_2 = Player('human')
            case '2':
                cls.player_1 = Player('human')
                cls.player_2 = Player('computer')

        # initialize game board
        cls.board = Board()

        # initialize pawns
        for num in range(1, 13):
            piece_w = Piece('white')
            piece_w.set_name('0x25CB')  # white
            cls.player_1.pieces.append(piece_w)
            piece_b = Piece('black')
            piece_b.set_name('0x25D9')  # black/ inverse white
            cls.player_2.pieces.append(piece_b)

        # TODO: test code
        # assign pieces to initial positions on board
        for line in range(len(cls.board.board_fields[1:4])):
            for column in range(len(cls.board.board_fields[line])):
                if cls.board.board_fields[line][column] == ' ':
                    cls.board.board_fields[line][column] = next(iter(cls.player_1.pieces))

        # TODO: test code
        for line in range(len(cls.board.board_fields[6:9])):
            for column in range(len(cls.board.board_fields[line])):
                if cls.board.board_fields[line][column] == ' ':
                    cls.board.board_fields[line][column] = next(iter(cls.player_2.pieces))

        # assign  initial field_list position to pieces
        for piece in cls.player_1.pieces:
            for line in range(len(cls.board.board_fields[1:4])):
                for column in range(len(cls.board.board_fields[line])):
                    if cls.board.board_fields[line][column] == piece:
                        piece.set_initial_position(convert(index=(line, column)))

        for piece in cls.player_1.pieces:
            for line in range(len(cls.board.board_fields[6:9])):
                for column in range(len(cls.board.board_fields[line])):
                    if cls.board.board_fields[line][column] == piece:
                        piece.set_initial_position(convert(index=(line, column)))

        cls.game_state = 'playing'

    # TODO: refactor code below
    @classmethod
    def check_coordinates(cls, field_no):
        while True:
            try:
                if field_no.upper() in Board.p_fields.keys():
                    return field_no
                else:
                    raise KeyError
            except KeyError:
                print("Incorrect input. The number you have provided is out of range!")

    @classmethod
    def check_owner(cls, field_no):
        while True:
            try:
                if Board.p_fields[field_no] not in cls.player_1.pieces:
                    raise ValueError
                return
            except ValueError:
                print("Sorry, you can only move your own pawns. Try again!")

    @classmethod
    def check_neighbours(cls, field_no):
        pass

    @classmethod
    def check_vacancy(cls, field_no):
        try:
            if not Board.is_cell_vacant(field_no):
                raise ValueError
            else:
                return field_no
        except ValueError:
            print("This field is occupied. Please choose another field!")

    @classmethod
    def play_vs_human(cls):
        # Player 1 move
        print("Player 1, Your turn!")
        pawn_address = input("Which pawn would you like to move? Please indicate its position: ")
        cls.check_coordinates(pawn_address)
        cls.check_owner(pawn_address)

        target_field = input("Where would you like to move your pawn? Please indicate target position: ")
        # check if target next to source - check_neighbours

        # check if fields forwards or backwards - check if included in array[row+1:] -
        # #TODO: func or include in piece constructor
        # check if target empty - check if cell vacant - func done
        # then move and change position - move -done
        try:

            if not Board.is_cell_vacant(target_field):
                raise ValueError
            else:
                Board.p_fields[target_field] = Board.p_fields[pawn_address]
                # update pawn position
        except ValueError:
            print("This field is occupied. Please choose another field!")

            # print("Player 2. Your turn now!") - when player 1 has finished - i.e. made a correct move

            # if not Board.is_cell_vacant(target_field) and Board.is_cell_vacant(Board.get_next_cell(target_field)):
            #     if Board.p_fields[target_field] in cls.player_2.pieces:
            #         cls.player_2.pieces.remove(Board.p_fields[target_field])
            #         cls.player_1.score += 1
            #         print("Good catch. You've captured your opponent's piece")
            #     else:
            #         print("This movement is not allowed!")
            # else:
            #     pass

            # check if field empty
            # if opponent piece in the way - check if next field empty

        @classmethod
        def show_current_score(cls):
            print()
            print(">>> Current score <<<")
            print(f"    Player 1: {cls.player_1.score}")
            print(f"    Player 2: {cls.player_2.score}")
            print()

        # player 1 move
        # check if own or enemy
        # check if target empty
        # move (define possible moves)

        # player 2 move
        # repeat the above

        # capturing
        # check if next field empty
        # check if other caputres possible - if yes lock other moves, must capture

        # monitor for promotion line

    @classmethod
    def human_vs_comp(cls):
        pass

    @classmethod
    def play_game(cls):
        pass


# manual test code
Game.initialize()
Game.board.display_board()
