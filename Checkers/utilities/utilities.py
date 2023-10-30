import string


def convert(index: tuple = None, field: str = None):
    rows_dict = {letter: string.ascii_uppercase[:8].index(letter) for letter in string.ascii_uppercase[:8]}
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
