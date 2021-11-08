def urlify(a: str, strlen: int) -> str:
    if not a:
        raise ValueError("Invalid str input")
    str_list: list[str] = list(a)
    end_str_pos: int = strlen - 1
    pos: int = len(a) - 1

    while pos > -1:
        if str_list[end_str_pos] != " ":
            str_list[pos] = str_list[end_str_pos]
        else:
            str_list[pos] = "0"
            str_list[pos-1] = "2"
            str_list[pos-2] = "%"
            pos -= 2
        pos -= 1
        end_str_pos -= 1

    return "".join(str_list)


if __name__ == "__main__":
    assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"
    assert urlify("Hey Bro  ", 7) == "Hey%20Bro"
    assert urlify("T his is a non sense sentence            ", 29) == "T%20his%20is%20a%20non%20sense%20sentence"
