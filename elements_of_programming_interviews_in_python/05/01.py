def sort_array_with_pivot(l: list[int], pivot_idx: int) -> list[int]:
    pivot = l[pivot_idx]

    smaller = 0
    for i in range(len(l)):
        if l[i] < pivot:
            l[i], l[smaller] = l[smaller], l[i]
            smaller += 1

    larger = len(l) - 1
    for i in reversed(range(len(l))):
        if l[i] < pivot:
            break
        if l[i] > pivot:
            l[i], l[larger] = l[larger], l[i]
            larger -= 1

    return l



if __name__ == "__main__":
    assert sort_array_with_pivot([1, 0, 0, 2, 2, 1, 1], 3) == [1, 0, 0, 1, 1, 2, 2]
