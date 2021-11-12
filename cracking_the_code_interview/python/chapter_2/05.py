from chapter_2.linked_list import LinkedList


def list_value(ll: LinkedList) -> int:
    l_value = 0
    aux = ll.head
    multiplier = 1
    while aux is not None:
        l_value += aux.value * multiplier
        aux = aux.next
        multiplier *= 10

    return l_value


def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    l1_value = list_value(ll1)
    l2_value = list_value(ll2)

    sum_value = l1_value + l2_value
    values = []
    # divmod
    total, value = divmod(sum_value, 10)
    values.append(value)
    while total != 0:
        total, value = divmod(total, 10)
        values.append(value)

    return LinkedList.from_value_list(list(reversed(values)))


if __name__ == "__main__":
    assert sum_lists(
        LinkedList.from_value_list([3, 2, 1]), LinkedList.from_value_list([3, 2, 1])
    ) == LinkedList.from_value_list([6, 4, 2])

    assert sum_lists(
        LinkedList.from_value_list([3, 2, 0]), LinkedList.from_value_list([3, 2, 0])
    ) == LinkedList.from_value_list([6, 4, 0])
