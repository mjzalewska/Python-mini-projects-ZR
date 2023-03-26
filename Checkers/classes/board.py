from Checkers.utilities.helper_functions import get_playable_fields, get_promotion_line_fields


class Board:
    playable_fields = get_playable_fields()
    promotion_line = get_promotion_line_fields(playable_fields)

    @classmethod
    def get_vacant_cells(cls, playable_fields):
        return {k: v for k, v in playable_fields.items() if not v}

    @classmethod
    def display_board(cls, playable_fields):
        pass




