import string
from Checkers.utils.helper_functions import get_playable_fields, get_promotion_line_fields


# TODO: include game fields, forbidden and promotion line definitions into Board definition
class Board:
    p_fields = get_playable_fields()
    promotion_line = get_promotion_line_fields(p_fields)

    @classmethod
    def get_vacant_cells(cls, p_fields):
        return {k: v for k, v in p_fields.items() if not v}

    @classmethod
    def is_cell_vacant(cls, cell):
        if not Board.p_fields[cell]:
            return True
        return False

    @classmethod
    def get_next_cell(cls, cell):  # change to calculate cells backwards (now it will only calc cells forwards)
        return f"{chr(ord(cell[0]) + 1)}{str(int(cell[1]) + 1)}"

    @classmethod
    def display_board(cls, p_fields):
        for num in range(1, 9):
            print(f'  {num}', end="")
        print(' ')
        for letter in string.ascii_uppercase[:8]:
            if letter in ['A', 'C', 'E', 'G']:
                print(f'{letter} \u25A0  {p_fields[f"{letter}2"]}  \u25A0  {p_fields[f"{letter}4"]}  \u25A0  '
                      f'{p_fields[f"{letter}6"]}  \u25A0  {p_fields[f"{letter}8"]}')
            else:
                print(f'{letter} {p_fields[f"{letter}1"]}  \u25A0  {p_fields[f"{letter}3"]}  \u25A0  '
                      f'{p_fields[f"{letter}5"]}  \u25A0  {p_fields[f"{letter}7"]}  \u25A0  ')


print(Board.get_next_cell("A2"))
