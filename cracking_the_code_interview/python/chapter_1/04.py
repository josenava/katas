def is_palindrome(a: str) -> bool:
    if not a:
        return False
    totals = []
    counter = 0
    sorted_str_list = sorted(a.lower())
    previous_char = sorted_str_list[0]
    for ch in sorted_str_list:
        if ch in (" ", ",", "."):
            continue
        if ch == previous_char:
            counter += 1
        else:
            totals.append(counter % 2)
            counter = 1
            previous_char = ch
    return sum(totals) <= 1


def is_palindrome_permutation(a: str) -> bool:
    if is_palindrome(a):
        is_permutation = False
        for i, _ in enumerate(a):
            if a[0+i].lower() != a[-1-i].lower():
                is_permutation = True
                break
        return is_permutation
    return False


if __name__ == "__main__":
    assert is_palindrome_permutation("Tact Coa")  # taco cat
    assert is_palindrome_permutation("yakka")  # kayak
    assert not is_palindrome_permutation("kayak")
    assert is_palindrome_permutation("leno mon meno lon")  # no lemon, no melon
    assert not is_palindrome_permutation("random")
