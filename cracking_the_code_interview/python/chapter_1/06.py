def compress_string(a: str) -> str:
    if not a:
        return a
    count = 0
    compressed_str = ""
    ch = a[0]
    for c in a:
        if c == ch:
            count += 1
        else:
            compressed_str += f"{ch}{count}"
            count = 1
            ch = c
    compressed_str += f"{ch}{count}"
    return compressed_str if len(compressed_str) < len(a) else a


if __name__ == "__main__":
    assert compress_string("aaabbcccddd") == "a3b2c3d3"
    assert compress_string("abc") == "abc"
    assert compress_string("abcaaaaaccccb") == "a1b1c1a5c4b1"
    assert compress_string("abbbbbb") == "a1b6"
