def is_rotation(s1: str, s2: str) -> bool:
    return s2 in s1+s1


if __name__ == "__main__":
    assert is_rotation("erbottlewat", "waterbottle")
    assert is_rotation("eriocandut", "canduterio")
