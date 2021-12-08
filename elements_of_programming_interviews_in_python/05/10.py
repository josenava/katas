from collections import defaultdict


def permutations(l: list, p: list[int]) -> list:
    p_idx = 0
    i = 0
    perm_elements = defaultdict(bool)

    while i < len(l):
        if not perm_elements[l[i]]:
            perm_elements[l[i]] = True
            l[p[i]], l[i] = l[i], l[p[i]]
        i += 1
    print(l)
    return l


if __name__ == "__main__":
    assert permutations(["a", "b", "c", "d"], [2, 0, 1, 3]) == ["b", "c", "a", "d"]
    assert permutations(["a", "b", "c", "d", "e"], [0, 1, 3, 2, 4]) == ["a", "b", "d", "c", "e"]

