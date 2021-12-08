def advance_game(l: list[int]) -> bool:
    max_position_reached = 0
    last_idx = len(l) - 1

    i = 0
    while i <= max_position_reached and max_position_reached <= last_idx:
        max_position_reached = max(max_position_reached, l[i] + i)
        i += 1

    return max_position_reached >= last_idx


if __name__ == "__main__":
    assert advance_game([3, 3, 1, 0, 2, 0, 1]) is True
    assert advance_game([3, 2, 0, 0, 2, 0, 1]) is False
