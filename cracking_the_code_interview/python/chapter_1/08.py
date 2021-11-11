def zero_matrix(m: list[list[int]]) -> list[list[int]]:
    positions_found: list[tuple[int, int]] = []
    for i in range(0, len(m)):
        for j in range(0, len(m[0])):
            if m[i][j] != 0:
                continue
            positions_found.append((i, j))

    for i, j in positions_found:
        for y in range(0, len(m[0])):
            m[i][y] = 0
        for x in range(0, len(m)):
            m[x][j] = 0

    return m


if __name__ == "__main__":
    assert zero_matrix([[1, 2], [2, 0], [3, 9]]) == [[1, 0], [0, 0], [3, 0]]
    assert zero_matrix([[2, 4, 5], [2, 2, 2], [0, 1, 0]]) == [[0, 4, 0], [0, 2, 0], [0, 0, 0]]
