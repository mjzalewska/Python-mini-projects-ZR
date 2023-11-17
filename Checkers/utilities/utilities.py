import string
from math import ceil
import Checkers.classes.board as b


def convert(index: tuple = None, field: str = None):
    rows_dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
    while True:
        try:
            if index is not None and field is None:
                row, column = index
                field_no = ''
                for k, v in rows_dict.items():
                    if v == row:
                        field_no += k
                field_no += str(column + 1)
                return field_no
            elif field is not None and index is None:
                return rows_dict[field[0]], int(field[1]) - 1
            else:
                raise TypeError
        except TypeError:
            print("Only one argument - index or field no - should be specified!")
            break


def get_piece_coordinates(old_position: str, target_position: str):
    old_line, old_column = convert(field=old_position)
    new_line, new_column = convert(field=target_position)
    mid_line, mid_column = ceil((old_line + new_line) / 2), ceil((old_column + new_column) / 2)
    return (old_line, old_column), (new_line, new_column), (mid_line, mid_column)


def get_piece_obj(current_line, current_column, mid_line, mid_column):
    current_piece = b.Board.fields[current_line][current_column]
    other_piece = b.Board.fields[mid_line][mid_column]
    return current_piece, other_piece
