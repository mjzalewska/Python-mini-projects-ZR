import random
from math import ceil

from art import tprint
from classes.piece import Pawn, King
from classes.player import Player
from classes.board import Board
import Checkers.utilities.utilities as utils


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
        cls.player_1.set_player_color(random.choice(['white', 'black']))
        if cls.player_1.color == 'white':
            cls.player_2.set_player_color('black')
        else:
            cls.player_2.set_player_color('white')

    @classmethod
    def decide_who_goes_first(cls):
        if cls.player_1.color == 'white':
            cls.current_player = cls.player_1
            cls.other_player = cls.player_2
        cls.current_player = cls.player_2
        cls.other_player = cls.player_1

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
                cls.player_1 = Player('human', cls.get_player_name('Player 1 enter your name: '))
                cls.player_2 = Player('human', cls.get_player_name('Player 2 enter your name: '))
            case '2':
                cls.player_1 = Player('human', cls.get_player_name('Player 1 enter your name: '))
                cls.player_2 = Player('CPU', 'Player 2')
        cls.assign_color()
        cls.decide_who_goes_first()

        # initialize game board
        cls.board = Board()

        # initialize pawns
        for num in range(1, 13):
            w_piece = Pawn(cls.player_1.color)
            cls.player_1.pieces.append(w_piece)

            b_piece = Pawn(cls.player_2.color)
            cls.player_2.pieces.append(b_piece)

        # assign pawns to initial positions on board
        p1_pieces_iter = iter(cls.player_1.pieces)
        for line in range(len(cls.board.fields[:3])):
            for column in range(len(cls.board.fields[line])):
                if cls.board.fields[line][column] == ' ':
                    p1_pawn = next(p1_pieces_iter)
                    cls.board.fields[line][column] = p1_pawn
                    p1_pawn.set_initial_position((line, column))

        p2_pieces_iter = iter(cls.player_2.pieces)
        for line in range(len(cls.board.fields[4:])):
            for column in range(len(cls.board.fields[line])):
                if cls.board.fields[-line][column] == ' ':
                    p2_pawn = next(p2_pieces_iter)
                    cls.board.fields[-line][column] = p2_pawn
                    p2_pawn.set_initial_position((line, column))

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
        (old_line, old_column), (new_line, new_column), (mid_line, mid_column) = \
            (utils.get_piece_coordinates(old_position, new_position))
        current_piece, other_piece = utils.get_piece_obj(old_line, old_column, mid_line, mid_column)
        if current_piece != ' ' and cls.is_owner_valid(current_piece, player):
            if current_piece.rank in ('pawn', 'king') and current_piece.is_move_allowed(cls.board.fields,
                                                                                        other_piece,
                                                                                        old_position):
                return True
            return False
        return False

    @classmethod
    def enforce_mandatory_move(cls, mandatory_moves):
        print(
            f'mandatory capture! You must move one of the following pieces: '
            f'{",".join([f"{move[0]}-> {move[1]}" for move in mandatory_moves])}')
        current_field = cls.get_player_input(prompt='Piece to move: ',
                                             validator=[move[0] for move in mandatory_moves],
                                             msg='Invalid choice! '
                                                 'Move not on the list')
        new_field = cls.get_player_input(prompt='Target location: ',
                                         validator=[move[1] for move in mandatory_moves if move[0] == current_field],
                                         msg='Invalid location! Please choose ')
        if cls.is_move_valid(current_field, new_field, cls.current_player):
            (line, column), (new_line, new_column), (mid_line, mid_column) = \
                (utils.get_piece_coordinates(current_field, new_field))
            piece, opponent_piece = utils.get_piece_obj(line, column, mid_line, mid_column)
            piece.move((new_line, new_column))
            opponent_piece.remove_piece('retired', cls.other_player)
            cls.current_player.update_score()
            if piece.rank == 'pawn' and piece.is_promoted():
                piece.promote_pawn()

    @classmethod
    def get_regular_move(cls):
        while True:
            current_field = cls.get_player_input('Piece to move: ',
                                                 [utils.convert(index=piece.position) for piece in
                                                  cls.current_player.pieces],
                                                 'Invalid choice! Please choose your own piece!')
            new_field = cls.get_player_input('Target location: ', cls.board.alfanum_field_list,
                                             'Location not on the board! Try again')
            try:
                if cls.is_move_valid(current_field, new_field, cls.current_player):
                    (line, column), (new_line, new_column), (mid_line, mid_column) = \
                        (utils.get_piece_coordinates(current_field, new_field))
                    piece = utils.get_piece_obj(line, column, mid_line, mid_column)[0]
                    piece.move((new_line, new_column))
                    if piece.rank == 'pawn' and piece.is_promoted():
                        piece.promote_pawn()
                else:
                    raise ValueError
            except ValueError:
                print('Invalid move! A pawn can only move forwards one field at a time!')

    @classmethod
    def switch_players(cls):
        if cls.current_player == cls.player_1:
            cls.current_player = cls.player_2
        cls.current_player = cls.player_1

    @classmethod
    def check_winner(cls):
        print(f'Current score: '
              f'{cls.player_1.name}: {cls.player_1.score}'
              f'{cls.player_2.name}: {cls.player_2.score}')
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
        ## check promotion and promote
        ## check if any movements left - check win
        ## check if any pawns left - check win
        ## switch sides

        if cls.game_state == 'initializing':  # fix the current player assignemnt
            cls.initialize()
        else:
            while not cls.game_over:
                print(Game.game_state)
                print(cls.current_player)
                print(cls.other_player)
                print("current player pieces:")
                for piece in cls.player_1.pieces:
                    print(piece.position)
                print("other player pieces")
                for piece in cls.player_2.pieces:
                    print(piece.position)
                print(cls.board.display_board())
                break
                # while True:
                #     mandatory_moves = cls.current_player.get_mandatory_captures(cls.board)
                #     if mandatory_moves:
                #         cls.enforce_mandatory_move(mandatory_moves)
                #         cls.board.display_board()
                #         if not cls.check_winner():
                #             cls.switch_players()
                #         else:
                #             cls.check_winner()
                #     else:
                #         cls.get_regular_move()
                #         cls.board.display_board
                #         if not cls.check_winner():
                #             cls.switch_players()
                #         else:
                #             cls.check_winner()
                #

        # add score display
        # add clear screen
        #  os.system('cls' if os.name == 'nt' else 'clear')
        # add winner check
        # side switch

    @classmethod
    def play_1p_game(cls):
        pass

    @classmethod
    def play(cls):
        pass


# manual test code
Game.initialize()
Game.play_2p_game()
