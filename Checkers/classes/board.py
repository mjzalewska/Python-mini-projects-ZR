import string
from Checkers.utilities.utilities import convert


class Board:
    w_box = '\u25A0'

    fields = [
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
    ]
    alfanum_field_list = [letter + str(num) for letter in string.ascii_uppercase[:8] for num in range(1, 9)]
    white_promotion_line = fields[0]
    black_promotion_line = fields[-1]

    @classmethod
    def is_cell_occupied(cls, cell):
        cell_line, cell_col = convert(field=cell)
        if cls.fields[cell_line][cell_col] != ' ':
            return True
        return False

    # @classmethod
    # def get_next_cell(cls, cell):
    #     return f"{chr(ord(cell[0]) + 1)}{str(int(cell[1]) + 1)}"
    #
    # @classmethod
    # def get_preceding_cell(cls, cell):
    #     return f"{chr(ord(cell[0]) - 1)}{str(int(cell[1]) - 1)}"

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
        print('   ' + '  '.join([str(num) for num in range(1, 9)]))
        letters = string.ascii_uppercase[:8]
        for i in range(len(letters)):
            print(f"{letters[i]}  {'  '.join(str_matrix[i])}")

