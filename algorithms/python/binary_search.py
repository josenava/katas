from typing import Optional


def binary_search(l: list[int], value: int) -> Optional[int]:
    lower_idx = 0
    upper_idx = len(l) - 1

    while lower_idx <= upper_idx:
        midpoint = (upper_idx + lower_idx) // 2
        if value == l[midpoint]:
            return midpoint
        if value < l[midpoint]:
            upper_idx = midpoint - 1
        elif value > l[midpoint]:
            lower_idx = midpoint + 1
    return None


if __name__ == "__main__":
    assert binary_search([3, 5, 6, 9, 10], 9) == 3
    assert binary_search([2, 4, 6, 7, 10], 11) is None
