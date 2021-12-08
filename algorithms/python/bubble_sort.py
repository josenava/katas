def bubble_sort(l: list[int]) -> list[int]:
    sorted = False
    unsorted_until_idx = len(l) - 1

    while not sorted:
        sorted = True
        for i in range(unsorted_until_idx):
            if l[i] > l[i+1]:
                print(f"Swap! {l[i]} <-> {l[i+1]}")
                l[i+1], l[i] = l[i], l[i+1]
                sorted = False
        unsorted_until_idx -= 1

    return l


if __name__ == "__main__":
    assert bubble_sort([3, 8, 4, 2, 7]) == [2, 3, 4, 7, 8]
