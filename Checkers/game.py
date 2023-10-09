import string
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

    # TODO: add rules ?
    @classmethod
    def show_welcome_screen(cls):
        tprint('Checkers', font='tarty1')  # tarty9
        print()

    @classmethod
    def game_over(cls):
        tprint('Game over', font='tarty1')

    @classmethod
    def show_menu(cls):
        pass

    @classmethod
    def show_rules(cls):
        pass

    @classmethod
    def choose_color(cls):
        pass

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
    def initialize(cls):
        # initialize players
        match Game.choose_game_mode():
            case '1':
                cls.player_1 = Player('human')
                cls.player_2 = Player('human')
            case '2':
                cls.player_1 = Player('human')
                cls.player_2 = Player('CPU')

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
    def scan_for_mandatory_jumps(cls, piece, player):
        mandatory_moves = []
        piece_coordinates = cls.board.get_piece_coordinates(piece)
        line, column = piece_coordinates[0]

        if line in range(0, len(cls.board.board_fields) - 1) and column in range(0, len(
                cls.board.board_fields[line]) - 1):
            left_down = cls.board.board_fields[line + 1][column - 1]
            right_down = cls.board.board_fields[line + 1][column + 1]
            left_top = cls.board.board_fields[line - 1][column - 1]
            right_top = cls.board.board_fields[line - 1][column + 1]

            next_left_down = cls.board.board_fields[line + 2][column - 2]
            next_right_down = cls.board.board_fields[line + 2][column + 2]
            next_left_top = cls.board.board_fields[line - 2][column - 2]
            next_right_top = cls.board.board_fields[line - 2][column + 2]

            if piece.rank == 'pawn':
                if left_down and left_down in player.pieces and next_left_down == ' ' or \
                        right_down and right_down in player.pieces and next_right_down == ' ':
                    mandatory_moves.append(convert(index=piece_coordinates[0]))

            elif piece.rank == 'king':
                if left_down and left_down in player.pieces and next_left_down == ' ' or \
                        right_down and right_down in player.pieces and next_right_down == ' ' or \
                        left_top and left_top in player.pieces and next_left_top == ' ' or \
                        right_top and right_top in player.pieces and next_right_top == ' ':
                    mandatory_moves.append(convert(index=piece_coordinates[0]))

        return mandatory_moves

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
    def check_vacancy(cls, field_no):
        try:
            if not Board.is_cell_vacant(field_no):
                raise ValueError
            else:
                return field_no
        except ValueError:
            print("This field is occupied. Please choose another field!")

    @classmethod
    def is_move_valid(cls, starting_position, ending_position, player):
        start_line, start_column = convert(field=starting_position)
        end_line, end_column = convert(field=ending_position)
        mid_line, mid_column = start_line + end_line / 2, start_column + end_column / 2
        current_piece = cls.board.board_fields[start_line][start_column]
        other_piece = cls.board.board_fields[mid_line][mid_column]
        if cls.is_owner_valid(current_piece, player):
            if current_piece.rank == "pawn":
                if current_piece.is_move_allowed(cls.board.board_fields, other_piece, starting_position, ending_position):
                    return True
            elif current_piece.rank == "king":
                if current_piece.is_move_allowed(cls.board.board_fields, other_piece, starting_position, ending_position):
                    return True
            return False
        return False

    @classmethod
    def is_movement_left(cls):
        pass

    @classmethod
    def is_piece_left(cls):
        pass

    def switch_players(self):
        pass

    @classmethod
    def play_vs_human(cls):
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
                    if cls.scan_for_mandatory_jumps(piece):
                        print('Mandatory jump! You must move one of the following pieces:')
                        for checker_field in cls.scan_for_mandatory_jumps(piece):
                            print(f'{checker_field}')
                        while True:
                            pawn_location = cls.get_field_no(
                                'Which piece would you like to move? Please indicate position '
                                'on the board: ')
                            try:
                                if pawn_location in cls.scan_for_mandatory_jumps(piece):
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
                                      f'{",".join(cls.scan_for_mandatory_jumps(piece))}')
                    else:
                        pawn_location = cls.get_field_no('Which pawn would you like to move? Please indicate position '
                                                         'on the board: ')
                        if not cls.board.is_cell_vacant(pawn_location) and \
                                cls.is_owner_valid(pawn_location, cls.player_1):
                            pass

                        target_location = cls.get_field_no('Where would you like to jump your pawn? Please indicate '
                                                           'position on the board: ')

        # check if distance correct (next field)
        # if the piece can jump this way (pawns only forwards, king - both ways)
        # check if empty

        # add a scan for compulsory capture
        # always check if moved to promotion line - promote if yes
        # win if other side no more moves available


    @classmethod
    def human_vs_comp(cls):
        pass

    @classmethod
    def play(cls):
        pass


# manual test code
Game.initialize()
Game.board.display_board()
