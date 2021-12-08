def word_parity(x: str) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result



if __name__ == "__main__":
    assert 1 == word_parity(0b1011)
    assert 0 == word_parity(0b10001000)

