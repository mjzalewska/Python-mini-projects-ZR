import random
from math import ceil

from art import tprint
from classes.piece import Pawn, King
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
    other_player = None

    @classmethod
    def print_welcome_screen(cls):
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
    def assign_color(cls):
        cls.player_1.color = random.choice(['white', 'black'])
        if cls.player_1.color == 'white':
            cls.player_2.set_color('black')
        else:
            cls.player_2.set_color('white')

    @classmethod
    def get_player_name(cls, prompt):
        while True:
            try:
                player_name = input(prompt)
                if not player_name:
                    raise ValueError
            except ValueError:
                player_name = 'Player' + str(Player.player_count)
            return player_name

    @classmethod
    def initialize(cls):
        # initialize players
        match Game.choose_game_mode():
            case '1':
                cls.player_1 = Player('human', cls.get_player_name())
                cls.player_2 = Player('human', cls.get_player_name())
            case '2':
                cls.player_1 = Player('human', cls.get_player_name())
                cls.player_2 = Player('CPU', 'Player 2')
        cls.assign_color()

        # initialize game board
        cls.board = Board()

        # initialize pawns
        for num in range(1, 13):
            w_piece = Pawn(cls.player_1.color)
            cls.player_1.pieces.append(w_piece)

            b_piece = Pawn(cls.player_2.color)
            cls.player_2.pieces.append(b_piece)

        # assign pawns to initial positions on board
        for line in range(len(cls.board.fields[:3])):
            for column in range(len(cls.board.fields[line])):
                if cls.board.fields[line][column] == ' ':
                    cls.board.fields[line][column] = next(iter(cls.player_1.pieces))

        for line in range(len(cls.board.fields[4:])):
            for column in range(len(cls.board.fields[line])):
                if cls.board.fields[-line][column] == ' ':
                    cls.board.fields[-line][column] = next(iter(cls.player_2.pieces))

        # assign  initial field_list position to pieces
        for item in cls.player_1.pieces:
            for line in range(len(cls.board.fields[:4])):
                for column in range(len(cls.board.fields[line])):
                    if cls.board.fields[line][column] == item:
                        item.set_initial_position((line, column))

        for item in cls.player_2.pieces:
            for line in range(len(cls.board.fields[5:])):
                for column in range(len(cls.board.fields[line])):
                    if cls.board.fields[line][column] == item:
                        item.set_initial_position((line, column))

        cls.game_state = 'playing'

    @classmethod
    def get_player_input(cls, prompt, validator, msg):
        while True:
            try:
                value = input(prompt)
                if value not in validator:
                    raise ValueError
                return value
            except ValueError:
                print(msg)

    @classmethod
    def is_owner_valid(cls, piece, player):
        while True:
            try:
                if piece.is_own_piece(player):
                    return True
                raise ValueError
            except ValueError:
                print("You can only move your own pawns!")

    @classmethod
    def check_if_field_vacant(cls, field_no):
        try:
            if not Board.is_cell_occupied(field_no):
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
        current_piece = cls.board.fields[old_line][old_column]
        other_piece = cls.board.fields[mid_line][mid_column]
        if current_piece != ' ' and cls.is_owner_valid(current_piece, player):
            if current_piece.rank == "pawn":
                if current_piece.is_move_allowed(cls.board.fields, other_piece, old_position):  # correct
                    return True
            elif current_piece.rank == "king":
                if current_piece.is_move_allowed(cls.board.fields, other_piece, old_position):  # correct
                    return True
            return False
        return False

    @classmethod
    def enforce_mandatory_jumps(cls, mandatory_moves):
        print(
            f'mandatory capture! You must move one of the following pieces: '
            f'{",".join([move[0] for move in mandatory_moves])}')
        current_field = cls.get_player_input(prompt='Piece to move: ',
                                             validator=[move[0] for move in mandatory_moves],
                                             msg='Invalid choice! '
                                                 'Move not on the list')
        new_field = cls.get_player_input(prompt='Target location: ',
                                         validator=[move[1] for move in mandatory_moves if move[0] == current_field],
                                         msg='Location not on the board! Try again')
        if cls.is_move_valid(current_field, new_field, cls.current_player):
            line, column = convert(field=current_field)
            new_line, new_column = convert(field=new_field)
            mid_line, mid_column = ceil((line + new_line) / 2), ceil((column + new_column) / 2)
            piece = cls.board.fields[line][column]
            opponent_piece = cls.board.fields[mid_line][mid_column]
            piece.move((new_line, new_column))
            opponent_piece.remove_piece('retired', cls.other_player)

    @classmethod
    def switch_players(cls):
        if cls.current_player == cls.player_1:
            cls.current_player = cls.player_2
        cls.current_player = cls.player_1

    @classmethod
    def check_winner(cls):
        if not cls.player_1.has_pieces_left() or not cls.player_1.has_moves_left(cls.board):
            print(f'{cls.player_2.name} wins!')
            return True
        elif not cls.player_2.has_pieces_left() or not cls.player_2.has_moves_left(cls.board):
            print(f'{cls.player_1.name} wins!')
            return True
        return False

    @classmethod
    def play_2p_game(cls):
        ## first check mandatory jumps then move
        ## validate movement
        ## check promotion
        ## check if any movements left
        ## check if any pawns left
        ## switch sides
        ## add scores (piece counts for each player)

        if cls.game_state == 'initializing':
            cls.initialize()
        else:
            while not cls.game_over:
                while True:
                    mandatory_moves = cls.current_player.get_mandatory_captures(cls.board)
                    if mandatory_moves:
                        cls.enforce_mandatory_jumps(mandatory_moves) # add promotion and win check
                        cls.board.display_board()
                    else:
                        break # add code for regular move

                current_field = cls.get_player_input('Piece to move: ', mandatory_moves, 'Invalid choice! '
                                                                                         'Move not on the list')
                new_field = cls.get_player_input('Target location: ', cls.board.alfanum_field_list,
                                                 'Location not on the board! Try again')
                while True:
                    try:
                        if cls.is_move_valid(current_field, new_field, cls.current_player):
                            line, column = convert(field=current_field)
                            new_line, new_column = convert(field=new_field)
                            piece = cls.board.fields[line][column]
                            piece.move((new_line, new_column))
                            if piece.is_promoted():
                                piece.promote_pawn()
                            if not cls.check_winner():
                                cls.switch_players()
                                break
                        else:
                            raise ValueError
                    except ValueError:
                        print('Invalid move! Try again!')
            else:
                pass

    @classmethod
    def play_1p_game(cls):
        pass

    @classmethod
    def play(cls):
        pass


# manual test code
Game.initialize()
Game.board.display_board()
