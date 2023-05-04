import string
from Checkers.utils.helper_functions import get_playable_fields, get_promotion_line_fields


class Board:
    p_fields = get_playable_fields()
    promotion_line = get_promotion_line_fields(p_fields)

    @classmethod
    def get_vacant_cells(cls, p_fields):
        return {k: v for k, v in p_fields.items() if not v}

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
