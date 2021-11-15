from typing import Optional

from chapter_2.linked_list import LinkedList, Node


def reverse_and_clone(n: Node) -> Node:
    head: Optional[Node] = None
    while n is not None:
        node = Node(n.value)
        node.next = head
        head = node
        n = n.next

    return head


def is_palindrome(ll: LinkedList) -> bool:
    if ll.head is None:
        return False
    aux = ll.head
    reversed_ll_head = reverse_and_clone(aux)

    while aux is not None and reversed_ll_head is not None:
        if aux.value != reversed_ll_head.value:
            return False
        aux = aux.next
        reversed_ll_head = reversed_ll_head.next

    if aux is not None or reversed_ll_head is not None:
        return False
    return True


if __name__ == "__main__":
    assert is_palindrome(LinkedList.from_value_list([1, 0, 0, 1]))
    assert is_palindrome(LinkedList.from_value_list([1, 0, 5, 0, 1]))
    assert not is_palindrome(LinkedList.from_value_list([1, 0, 6, 7, 5, 0, 1]))
