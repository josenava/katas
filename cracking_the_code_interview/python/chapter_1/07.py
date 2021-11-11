def rot90(m: list[list[int]]) -> list[list[int]]:
    """Assuming valid input"""
    print(m)
    n = len(m)
    for layer in range(0, n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = m[first][i]
            # left -> top
            m[first][i] = m[last-offset][first]
            # bottom -> left
            m[last-offset][first] = m[last][last-offset]
            # right -> bottom
            m[last][last-offset] = m[i][last]
            # top -> right
            m[i][last] = top

    return m


if __name__ == "__main__":
    assert rot90([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]
    assert rot90([[6, 9, 4], [1, 8, 7], [5, 3, 2]]) == [[5, 1, 6], [3, 8, 9], [2, 7, 4]]
