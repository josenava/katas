from chapter_2.linked_list import LinkedList, Node


def delete_middle_node(n: Node) -> None:
    next = n.next
    n.value = next.value
    n.next = next.next


if __name__ == "__main__":
    ll = LinkedList.from_value_list([1, 3, 8, 5, 7, 9, 10])
    val = 8
    aux = ll.head
    while aux.value != val:
        aux = aux.next
    delete_middle_node(aux)

    assert ll == LinkedList.from_value_list([1, 3, 5, 7, 9, 10])
