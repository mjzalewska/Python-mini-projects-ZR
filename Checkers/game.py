import random
import string
from math import ceil

from art import tprint
from classes.piece import WhitePawn, BlackPawn, WhiteKing, BlackKing
from classes.player import Player
from classes.board import Board
from Checkers.utilities.utilities import convert


class Game:
    game_state = 'initializing'
    game_over = False
    board = None
    player_1 = None
    player_2 = None
    current_player = None

    @classmethod
    def show_welcome_screen(cls):
        tprint('Checkers', font='tarty1')  # tarty9
        print()

    @classmethod
    def print_game_over(cls):
        tprint('Game over', font='tarty1')

    @classmethod
    def choose_game_mode(cls):
        modes = ['1', '2']
        print('Please choose game mode: ')
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
    def choose_color(cls):
        return random.choice(["white", "black"])

    @classmethod
    def initialize(cls):
        # initialize players
        match Game.choose_game_mode():
            case '1':
                cls.player_1 = Player('human', 'white')
                cls.player_2 = Player('human', 'black')
            case '2':
                cls.player_1 = Player('human', 'white')
                cls.player_2 = Player('CPU', 'black')

        # initialize game board
        cls.board = Board()

        # initialize pawns
        for num in range(1, 13):
            w_piece = WhitePawn()
            cls.player_1.pieces.append(w_piece)

            b_piece = BlackPawn()
            cls.player_2.pieces.append(b_piece)

        # assign pawns to initial positions on board
        for line in range(len(cls.board.board_fields[:3])):
            for column in range(len(cls.board.board_fields[line])):
                if cls.board.board_fields[line][column] == ' ':
                    cls.board.board_fields[line][column] = next(iter(cls.player_1.pieces))

        for line in range(len(cls.board.board_fields[4:])):
            for column in range(len(cls.board.board_fields[line])):
                if cls.board.board_fields[-line][column] == ' ':
                    cls.board.board_fields[-line][column] = next(iter(cls.player_2.pieces))

        # assign  initial field_list position to pieces
        for item in cls.player_1.pieces:
            for line in range(len(cls.board.board_fields[:4])):
                for column in range(len(cls.board.board_fields[line])):
                    if cls.board.board_fields[line][column] == item:
                        item.set_initial_position((line, column))

        for item in cls.player_2.pieces:
            for line in range(len(cls.board.board_fields[5:])):
                for column in range(len(cls.board.board_fields[line])):
                    if cls.board.board_fields[line][column] == item:
                        item.set_initial_position((line, column))

        cls.game_state = 'playing'

    @classmethod
    def scan_for_mandatory_captures(cls, player):
        mandatory_captures = []
        for piece in player.pieces:
            if piece.rank == 'pawn':
                if piece.color == 'white':
                    dirs = [[2, -2], [2, 2]]
                else:
                    dirs = [[-2, -2], [-2, 2]]
            else:
                dirs = [[2, -2], [2, 2], [-2, -2], [-2, 2]]

            for d in dirs:
                target_field = (piece.position[0] + d[0], piece.position[1] + d[1])
                if piece.is_move_allowed(cls.board, target_field, player, piece.color):
                    mandatory_captures.append(convert(index=target_field))
        return mandatory_captures

    @classmethod
    def get_field_no(cls, prompt):
        board_field_list = [letter + str(num) for letter in string.ascii_uppercase[:8] for num in range(1, 9)]
        while True:
            try:
                field_no = input(prompt)
                if field_no not in board_field_list:
                    raise ValueError
                else:
                    return field_no
            except ValueError:
                print('The location is not on the board!')

    @classmethod
    def is_owner_valid(cls, piece, player):
        while True:
            try:
                if piece.is_own_piece(player, cls.board):
                    return True
                raise ValueError
            except ValueError:
                print("You can only move your own pawns!")

    @classmethod
    def check_if_field_vacant(cls, field_no):
        try:
            if not Board.is_cell_vacant(field_no):
                raise ValueError
            else:
                return field_no
        except ValueError:
            print("This field is occupied. Please choose another field!")

    @classmethod
    def is_move_valid(cls, old_position, new_position, player):
        old_line, old_column = convert(field=old_position)
        new_line, new_column = convert(field=new_position)
        mid_line, mid_column = ceil((old_line + new_line) / 2), ceil((old_column + new_column) / 2)
        current_piece = cls.board.board_fields[old_line][old_column]
        other_piece = cls.board.board_fields[mid_line][mid_column]
        if current_piece != ' ' and cls.is_owner_valid(current_piece, player):
            if current_piece.rank == "pawn":
                if current_piece.is_move_allowed(cls.board.board_fields, other_piece, old_position):
                    return True
            elif current_piece.rank == "king":
                if current_piece.is_move_allowed(cls.board.board_fields, other_piece, old_position):
                    return True
            return False
        return False

    @classmethod
    def switch_players(cls):
        if cls.current_player == "white":
            cls.current_player = "black"
        cls.current_player = "white"

    @classmethod
    def play_vs_human(cls):
        ## change Piece code, change mandatory jumps code
        ## first check mandatory jumps then move
        ## validate movement
        ## check promotion
        ## check if any movements left
        ## check if any pawns left
        ## switch sides
        while True:
            if cls.game_state == 'initializing':
                cls.initialize()
            else:
                print('Player 1, your turn!')
                for piece in cls.player_1.pieces:
                    if cls.scan_for_mandatory_captures(piece, ):
                        print('Mandatory jump! You must move one of the following pieces:')
                        for checker_field in cls.scan_for_mandatory_captures(piece, ):
                            print(f'{checker_field}')
                        while True:
                            pawn_location = cls.get_field_no(
                                'Which piece would you like to move? Please indicate position '
                                'on the board: ')
                            try:
                                if pawn_location in cls.scan_for_mandatory_captures(piece, ):
                                    target_location = cls.get_field_no(
                                        'Where would you like to move your pawn? Please indicate '
                                        'position on the board: ')
                                    for item in cls.board.get_board_diagonals(pawn_location):
                                        # check if target field is next to the current field and empty or target field is
                                        # two fields from the current one, enemy pawn is in the way and the target field is empty
                                        try:
                                            if (item.index(target_location) == item.index(pawn_location) + 1 and not
                                            item[item.index(target_location)]) or \
                                                    (item.index(target_location) == item.index(pawn_location) + 2 and
                                                     item[item.index(target_location) - 1] and not item[
                                                                item.index(target_location)]):
                                                # move and remove from gameplay
                                                pass
                                            else:
                                                raise ValueError
                                        except ValueError:
                                            print("Forbidden move!")
                                            ### przepisać to z wykorzystaniem obiektu Piece
                                            # czy pion obok to pion przeciwnika (powinno być item[item.index(target_location)-1] jest pionem przecienika)
                                            # różnicowanie ruchu pion vs damka
                                            # wielobicie
                                            # spr czy osiągnięta linia przemiany
                                else:
                                    raise ValueError
                            except ValueError:
                                print(f'You can only move one of the following pawns: '
                                      f'{",".join(cls.scan_for_mandatory_captures(piece, ))}')
                    else:
                        pawn_location = cls.get_field_no('Which pawn would you like to move? Please indicate position '
                                                         'on the board: ')
                        if not cls.board.is_cell_vacant(pawn_location) and \
                                cls.is_owner_valid(pawn_location, cls.player_1):
                            pass

                        target_location = cls.get_field_no('Where would you like to jump your pawn? Please indicate '
                                                           'position on the board: ')


    @classmethod
    def human_vs_comp(cls):
        pass

    @classmethod
    def play(cls):
        pass


# manual test code
Game.initialize()
Game.board.display_board()
