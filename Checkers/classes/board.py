import string
from Checkers.utilities.utilities import convert


class Board:
    w_box = '\u25A0'

    board_fields = [
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
        [w_box, ' ', w_box, ' ', w_box, ' ', w_box, ' '],
        [' ', w_box, ' ', w_box, ' ', w_box, ' ', w_box],
    ]
    white_promotion_line = board_fields[0]
    black_promotion_line = board_fields[-1]

    @classmethod
    def get_vacant_cells(cls):  ## redundant ??
        vacant_cells = []
        for line in range(len(cls.board_fields)):
            for column in range(len(cls.board_fields[line])):
                if cls.board_fields[line][column] == ' ':
                    vacant_cells.append((line, column))
        return vacant_cells

    @classmethod
    def is_cell_vacant(cls, cell):
        cell_line, cell_col = convert(field=cell)
        if cls.board_fields[cell_line][cell_col] == ' ':
            return True
        return False

    @classmethod
    def get_next_cell(cls, cell):
        return f"{chr(ord(cell[0]) + 1)}{str(int(cell[1]) + 1)}"

    @classmethod
    def get_preceding_cell(cls, cell):
        return f"{chr(ord(cell[0]) - 1)}{str(int(cell[1]) - 1)}"

    @classmethod
    def get_board_diagonals(cls, field):
        diagonal_elements = [[], []]
        field_line, field_column = convert(field=field)

        # first diag
        for line_idx in range(len(cls.board_fields)):
            for col_idx in range(len(cls.board_fields[line_idx])):
                if col_idx == -line_idx + (field_line + field_column):
                    if cls.board_fields[line_idx][col_idx] == ' ':
                        diagonal_elements[0].append(convert(index=(line_idx, col_idx)))
                    else:
                        diagonal_elements[0].append(cls.board_fields[line_idx][col_idx])
        # second diag
        for line_idx in range(len(cls.board_fields)):
            for col_idx in range(len(cls.board_fields[line_idx])):
                if col_idx == line_idx - (field_line - field_column):
                    if cls.board_fields[line_idx][col_idx] == ' ':
                        diagonal_elements[1].append(convert(index=(line_idx, col_idx)))
                    else:
                        diagonal_elements[1].append(cls.board_fields[line_idx][col_idx])

        return diagonal_elements

    # will not work - get diagonals returns two lists of piece obj in diagonals
    @classmethod
    def is_cell_in_line(cls, source_field, target_field):
        for diagonal in cls.get_board_diagonals(source_field):
            if target_field in diagonal:
                return True
            return False

    @classmethod
    def is_next_cell(cls, source_field, target_field):
        pass

    @classmethod
    def get_piece_coordinates(cls, piece_obj):
        coordinates = [(line, column) for line in range(len(cls.board_fields))
                       for column in range(len(cls.board_fields[line]))
                       if cls.board_fields[line][column] == piece_obj]
        return coordinates

    @classmethod
    def display_board(cls):
        str_matrix = []
        for line in cls.board_fields:
            str_matrix.append([str(column) for column in line])
        print('   ' + '  '.join([str(num) for num in range(1, 9)]))
        letters = string.ascii_uppercase[:8]
        for i in range(len(letters)):
            print(f"{letters[i]}  {'  '.join(str_matrix[i])}")

