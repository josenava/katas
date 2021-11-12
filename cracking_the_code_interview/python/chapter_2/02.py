from chapter_2.linked_list import LinkedList


def kth_to_last(ll: LinkedList, k: int) -> list[int]:
    value_list = []
    pos = 1
    aux = ll.head
    while aux is not None:
        if pos >= k:
            value_list.append(aux.value)

        pos += 1
        aux = aux.next
    return value_list


if __name__ == "__main__":
    assert kth_to_last(LinkedList.from_value_list([1, 3, 9, 9, 30, 1]), 3) == [9, 9, 3, 1]
    assert kth_to_last(LinkedList.from_value_list([1, 3]), 1) == [3, 1]
