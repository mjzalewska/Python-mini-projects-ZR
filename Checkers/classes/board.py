import string

from termcolor import colored

import Checkers.utilities.utilities as utils


class Board:
    w_sq = '\u25A0'

    fields = [
        [w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq, ' '],
        [' ', w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq],
        [w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq, ' '],
        [' ', w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq],
        [w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq, ' '],
        [' ', w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq],
        [w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq, ' '],
        [' ', w_sq, ' ', w_sq, ' ', w_sq, ' ', w_sq],
    ]
    alfanum_field_list = [letter + str(num) for letter in string.ascii_uppercase[:8] for num in range(1, 9)]
    white_promotion_line = None
    black_promotion_line = None

    @classmethod
    def is_cell_occupied(cls, cell):
        cell_line, cell_col = utils.convert(field=cell)
        if cls.fields[cell_line][cell_col] != ' ':
            return True
        return False

    @classmethod
    def get_piece_coordinates(cls, piece_obj):
        coordinates = [(line, column) for line in range(len(cls.fields))
                       for column in range(len(cls.fields[line]))
                       if cls.fields[line][column] == piece_obj]
        return coordinates

    @classmethod
    def display_board(cls):
        str_matrix = []
        for line in cls.fields:
            str_matrix.append([str(column) for column in line])
        print('\t' + ('\t'.join([str(num) for num in range(1, 9)])))
        letters = string.ascii_uppercase[:8]
        for i in range(len(letters)):
            print(f"{letters[i]}" + '\t' + '\t'.join(str_matrix[i]))
