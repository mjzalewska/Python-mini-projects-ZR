import os
import random
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
            print(f'{cls.current_player.name} your color is {cls.current_player.color}, you will move first!\n')
        else:
            cls.current_player = cls.player_2
            print(f'{cls.current_player.name} your color is {cls.current_player.color}, you will move first!\n')
            cls.other_player = cls.player_1

    @classmethod
    def get_player_name(cls, prompt):
        while True:
            try:
                player_name = input(prompt)
                if not player_name:
                    raise ValueError
            except ValueError:
                player_name = 'Player ' + str(Player.player_count + 1)
            return player_name

    @classmethod
    def initialize(cls, mode):
        # initialize players
        match mode:
            case '1':
                cls.player_1 = Player('human', cls.get_player_name('Player 1 enter your name: '), 'top')
                cls.player_2 = Player('human', cls.get_player_name('Player 2 enter your name: '), 'bottom')
            case '2':
                cls.player_1 = Player('human', cls.get_player_name('Player 1 enter your name: '), 'top')
                cls.player_2 = Player('CPU', 'Player 2', 'bottom')
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
        for line in range(3):
            for column in range(8):
                if cls.board.fields[line][column] == ' ':
                    p1_pawn = next(p1_pieces_iter)
                    cls.board.fields[line][column] = p1_pawn
                    p1_pawn.set_position((line, column))

        p2_pieces_iter = iter(cls.player_2.pieces)
        for line in range(1, 4):
            for column in range(8):
                if cls.board.fields[line + 4][column] == ' ':
                    p2_pawn = next(p2_pieces_iter)
                    cls.board.fields[line + 4][column] = p2_pawn
                    p2_pawn.set_position((line + 4, column))

        # set promotion lines
        if cls.player_1.color == 'white':
            cls.board.white_promotion_line = cls.board.fields[0]
            cls.board.black_promotion_line = cls.board.fields[-1]
        else:
            cls.board.white_promotion_line = cls.board.fields[-1]
            cls.board.black_promotion_line = cls.board.fields[0]

        cls.game_state = 'playing'

    @classmethod
    def get_player_input(cls, prompt, validator, msg):
        while True:
            try:
                value = input(prompt).upper()
                if value not in validator:
                    raise ValueError
                return value
            except ValueError:
                print(msg)

    @classmethod
    def clear_screen(cls):
        if os.name == 'nt':
            os.system('cls')
        os.system('clear')

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
    def is_move_valid(cls, current_position, new_position, player):
        (current_line, current_column), (new_line, new_column), (mid_line, mid_column) = \
            (utils.get_piece_coordinates(current_position, new_position))
        current_piece = utils.get_piece_obj(current_line, current_column, mid_line, mid_column, cls.board)[0]
        if (current_piece != ' ' and cls.is_owner_valid(current_piece, player) and
                current_piece.rank == 'pawn' and current_piece.is_move_allowed(cls.board, new_position,
                                                                               cls.current_player)):
            return True
        elif (current_piece != ' ' and cls.is_owner_valid(current_piece, player) and
              current_piece.rank == 'king' and current_piece.is_move_allowed(cls.board, new_position,
                                                                             cls.current_player)):
            return True
        else:
            return False

    @classmethod
    def enforce_mandatory_move(cls, mandatory_moves):
        print(f'{cls.current_player.name} ({cls.current_player.color}) your move!')
        print(
            f'Mandatory capture! You must move one of the following pieces: '
            f'{",".join([f"{move[0]}-> {move[1]}" for move in mandatory_moves])}')
        current_field = cls.get_player_input(prompt='Piece to move: ',
                                             validator=[move[0] for move in mandatory_moves],
                                             msg='Invalid choice! '
                                                 'Move not on the list')
        new_field = cls.get_player_input(prompt='Target location: ',
                                         validator=[move[1] for move in mandatory_moves if move[0] == current_field],
                                         msg='Invalid location!')
        if cls.is_move_valid(current_field, new_field, cls.current_player):
            (line, column), (new_line, new_column), (mid_line, mid_column) = \
                (utils.get_piece_coordinates(current_field, new_field))
            piece, opponent_piece = utils.get_piece_obj(line, column, mid_line, mid_column, cls.board)
            piece.move((new_line, new_column), cls.board)
            opponent_piece.remove_piece('retired', cls.other_player, cls.board)
            cls.current_player.update_score()
            if piece.rank == 'pawn' and piece.is_promoted(cls.board):
                piece.promote_pawn(cls.board, cls.current_player)
            cls.switch_players()

    @classmethod
    def get_regular_move(cls):
        while True:
            print(f'{cls.current_player.name} ({cls.current_player.color}) your move!')
            current_field = cls.get_player_input('Piece to move: ',
                                                 [utils.convert(index=piece.position) for piece in
                                                  cls.current_player.pieces],
                                                 'Invalid choice! Please choose one of your pieces to move')

            new_field = cls.get_player_input('Target location: ', cls.board.alfanum_field_list,
                                             'Invalid field number! Try again')
            try:
                if cls.is_move_valid(current_field, new_field, cls.current_player):
                    (current_line, current_column), (new_line, new_column), (mid_line, mid_column) = \
                        (utils.get_piece_coordinates(current_field, new_field))
                    piece, opponent_piece = utils.get_piece_obj(current_line, current_column, mid_line, mid_column,
                                                                cls.board)
                    if abs(new_line - current_line) == 1 and abs(new_column - current_column) == 1:
                        piece.move((new_line, new_column), cls.board)
                    elif abs(new_line - current_line) == 2 and abs(new_column - current_column) == 2:
                        piece.move((new_line, new_column), cls.board)
                        opponent_piece.remove_piece('retired', cls.other_player, cls.board)
                        cls.current_player.update_score()
                    if piece.rank == 'pawn' and piece.is_promoted(cls.board):
                        piece.promote_pawn(cls.board, cls.current_player)
                    # cls.clear_screen()
                    cls.board.display_board()
                    cls.switch_players()
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Invalid move!')

    @classmethod
    def switch_players(cls):
        if cls.current_player == cls.player_1:
            cls.current_player = cls.player_2
            cls.other_player = cls.player_1
        elif cls.current_player == cls.player_2:
            cls.current_player = cls.player_1
            cls.other_player = cls.player_2

    @classmethod
    def check_winner(cls):
        print(f'Current score: \n'
              f'{cls.player_1.name}: {cls.player_1.score}\n'
              f'{cls.player_2.name}: {cls.player_2.score}')
        if not cls.player_1.has_piece_left() or not cls.player_1.has_moves_left(cls.board):
            print(f'{cls.player_2.name} wins!')
            return True
        elif not cls.player_2.has_piece_left() or not cls.player_2.has_moves_left(cls.board):
            print(f'{cls.player_1.name} wins!')
            return True
        return False

    @classmethod
    def print_ui_message(cls, message):
        tprint(message, font='tarty1')

    @classmethod
    def play_2p_game(cls):
        ## first check mandatory jumps then move
        ## validate movement
        ## check promotion and promote
        ## check if any movements left - check win
        ## check if any pawns left - check win
        ## switch sides

        # mandatory: dodać try/except w enforce mandatory... oraz while
        # za pierwszym razem spr wszystkie, ale potem już tylko spr kolejne dla danego pionka
        # game over - po komunikacje 'xy wins" nadal pyta o ruch drugą stronę
        # plansza drukuje się podwójnie

        while True:
            mandatory_moves = cls.current_player.get_mandatory_captures(cls.board)
            if mandatory_moves:
                cls.board.display_board()
                print()
                cls.enforce_mandatory_move(mandatory_moves)
                print()
                if cls.check_winner():
                    cls.game_over = True
            else:
                cls.board.display_board()
                print()
                cls.get_regular_move()
                print()
                if cls.check_winner():
                    cls.game_over = True

    @classmethod
    def play_1p_game(cls):
        pass

    @classmethod
    def play(cls):
        game_mode = cls.choose_game_mode()
        match game_mode:
            case '1':
                while not cls.game_over:
                    if cls.game_state == 'initializing':
                        cls.initialize(game_mode)
                    else:
                        cls.play_2p_game()

            case '2':
                pass


Game.play()
