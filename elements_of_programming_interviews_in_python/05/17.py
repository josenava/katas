from copy import deepcopy


def has_duplicates(l: list[int]) -> bool:
    raw_values = [i for i in l if i != 0]
    values = set(raw_values)

    return len(values) != len(raw_values)


def check_rows_and_columns(sudoku: list[list[int]]) -> bool:
    for r in range(len(sudoku)):
        if has_duplicates(sudoku[r]):
            return False
        col_values = []
        for c in range(len(sudoku)):
            col_values.append(sudoku[c][r])

        if has_duplicates(col_values):
            return False

    return True


def check_sub_grid(m: list[list[int]]) -> bool:
    values = []
    for i in range(len(m)):
        for j in range(len(m)):
            values.append(m[i][j])

    return not has_duplicates(values)


def check_sub_grids(sudoku: list[list[int]]) -> bool:
    for i in range(0, len(sudoku), 3):
        if not check_sub_grid([r[i:i+3] for r in sudoku[i:i+3]]):
            return False
    return True

    
def check_valid_partial_sudoku(sudoku: list[list[int]]) -> bool:
    return check_rows_and_columns(sudoku) and check_sub_grids(sudoku)


if __name__ == "__main__":
    s_0 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    s_1 = deepcopy(s_0)
    s_2 = deepcopy(s_0)
    s_3 = deepcopy(s_0)
    assert check_valid_partial_sudoku(s_0)
    s_1[0][0] = 3
    assert not check_valid_partial_sudoku(s_1)
    s_2[2][0] = 4
    assert not check_valid_partial_sudoku(s_2)
    s_3[3][3] = 3
    assert not check_valid_partial_sudoku(s_3)
