def is_unique(a: str) -> bool:
    """Assuming a is an ASCII char"""
    if not a or len(a) > 128:
        return False
    existing_chars = [False for _ in range(128)]
    for ch in a:
        int_val = ord(ch)
        if existing_chars[int_val]:
            return False
        existing_chars[int_val] = True
    return True


if __name__ == "__main__":
    assert not is_unique("")
    assert is_unique("ab")
    assert not is_unique("baaaab")
    assert is_unique("ba")
    assert not is_unique("abcda")
