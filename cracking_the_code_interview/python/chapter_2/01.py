from collections import defaultdict

from chapter_2.linked_list import LinkedList


def remove_dups(ll: LinkedList) -> LinkedList:
    elements = defaultdict(bool)
    aux = ll.head
    prev = None
    while aux is not None:
        if elements[aux.value]:
            # delete
            prev.next = aux.next
        else:
            elements[aux.value] = True
            prev = aux
        aux = aux.next

    return ll


if __name__ == "__main__":
    assert remove_dups(LinkedList.from_value_list([1, 8, 2, 2, 9, 2, 3])) == LinkedList.from_value_list([1, 8, 9, 2, 3])
    assert remove_dups(LinkedList.from_value_list([1, 8, 2, 1])) == LinkedList.from_value_list([8, 2, 1])
