def is_permutation(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    assert is_permutation("", "")
    assert is_permutation("ababa", "bbaaa")
    assert not is_permutation("cbb", "bcc")
    assert not is_permutation("nbaaaabj", "jbnbaa")
