def delete_repeated_elements(l: list[int]) -> tuple[int, list[int]]:
    if not l:
        raise ValueError("Invalid list")

    write_idx = 1
    for i in range(1, len(l)):
        if l[write_idx - 1] != l[i]:
            l[write_idx] = l[i]
            write_idx += 1
    return write_idx, l
            



if __name__ == "__main__":
    assert delete_repeated_elements([1, 1, 2, 3, 3, 5, 5, 5]) == (4, [1, 2, 3, 5, 3, 5, 5, 5])
    assert delete_repeated_elements([5, 5, 5, 8, 9, 10]) == (4, [5, 8, 9, 10, 9, 10])
