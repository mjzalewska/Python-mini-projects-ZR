import string


# generate a dict of playable field_list fields (dark only)
def get_playable_fields():
    playable_fields = {}
    for letter in string.ascii_uppercase[:8]:
        for num in range(2, 10, 2):
            if letter in ['A', 'C', 'E', 'G']:
                playable_fields[f'{letter}{num}'] = ' '
            else:
                playable_fields[f'{letter}{num - 1}'] = ' '
    return playable_fields


# get promotion line fields
def get_promotion_line_fields(playable_fields):
    promotion_line = {}
    for key, value in playable_fields.items():
        if key[0] in ['A', 'H']:
            promotion_line[key] = value
    return promotion_line