from chapter_2.linked_list import LinkedList, Node


def partition(ll: LinkedList, k: int) -> LinkedList:
    ll_gte = LinkedList()
    ll_lt = LinkedList()
    aux = ll.head

    while aux is not None:
        if aux.value < k:
            ll_lt.add(Node(aux.value))
        else:
            ll_gte.add(Node(aux.value))
        aux = aux.next

    # reusing ll_lt
    ll_lt_aux = ll_lt.head
    while ll_lt_aux.next is not None:
        ll_lt_aux = ll_lt_aux.next

    # now ll_lt_aux is at last element of ll_lt
    ll_lt_aux.next = ll_gte.head

    return ll_lt


if __name__ == "__main__":
    expected_ll = LinkedList.from_value_list([10, 4, 9, 8, 7, 3, 2, 2, 1])
    assert partition(
        LinkedList.from_value_list([1, 7, 8, 2, 2, 9, 4, 3, 10]), 4
    ) == expected_ll
