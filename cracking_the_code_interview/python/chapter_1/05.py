def is_one_or_zero_away(a: str, b: str) -> bool:
    len_diff = len(a) - len(b)
    if abs(len_diff) > 1:
        return False
    edits = 0
    if len_diff == 0:
        # replace operation
        for i in range(len(a)):
            if edits > 1:
                break
            if a[i] != b[i]:
                edits += 1
    else:
        # insert or delete operation
        i = 0
        j = 0
        shorter_str = a if len_diff < 0 else b
        greater_str = b if shorter_str == a else a
        while i < len(shorter_str) and j < len(greater_str):
            if shorter_str[i] != greater_str[j]:
                if i != j:
                    return False
                j += 1
            else:
                i += 1
                j += 1

    return edits <= 1


if __name__ == "__main__":
    assert is_one_or_zero_away("pale", "bale")
    assert not is_one_or_zero_away("pale", "pl")
    assert not is_one_or_zero_away("pale", "bake")
    assert is_one_or_zero_away("pale", "ple")
    assert is_one_or_zero_away("pales", "pale")
