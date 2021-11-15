from typing import Optional

from chapter_2.linked_list import LinkedList, Node


def is_intersection_suboptimal(ll1: LinkedList, ll2: LinkedList) -> tuple[bool, Optional[Node]]:
    l1_aux = ll1.head
    l2_aux = ll2.head

    while l1_aux is not None:
        while l2_aux is not None:
            if l1_aux is l2_aux:
                return True, l1_aux
            l2_aux = l2_aux.next
        l1_aux = l1_aux.next
        l2_aux = ll2.head

    return False, None


def is_intersection(ll1: LinkedList, ll2: LinkedList) -> tuple[bool, Optional[Node]]:
    if ll1.head is None or ll2.head is None:
        return False, None
    len1 = 1
    len2 = 1
    aux_ll1 = ll1.head
    aux_ll2 = ll2.head
    while aux_ll1.next is not None:
        len1 += 1
        aux_ll1 = aux_ll1.next

    while aux_ll2.next is not None:
        len2 += 1
        aux_ll2 = aux_ll2.next

    if aux_ll1 is not aux_ll2:
        return False, None

    ll_shorter = ll1 if len2 >= len1 else ll2
    ll_longer = ll2 if len2 >= len1 else ll1
    diff = abs(len2 - len1)
    pos = 0
    aux_longer = ll_longer.head
    while pos < diff:
        pos += 1
        aux_longer = aux_longer.next

    aux_shorter = ll_shorter.head
    while aux_longer is not None:
        if aux_longer is aux_shorter:
            return True, aux_longer
        aux_longer = aux_longer.next
        aux_shorter = aux_shorter.next

    return False, None


if __name__ == "__main__":
    intersect_node = Node(321)
    following_node_1 = Node(123)
    following_node_2 = Node(333)

    ll1 = LinkedList.from_value_list([9, 8])
    ll1.add(intersect_node)
    ll1.add(following_node_1)
    ll1.add(following_node_2)

    ll2 = LinkedList.from_value_list([4, 4, 56])
    aux = ll2.head
    while aux.next is not None:
        aux = aux.next
    aux.next = intersect_node

    assert is_intersection_suboptimal(ll1, ll2) == (True, intersect_node)
    assert is_intersection(ll1, ll2) == (True, intersect_node)

    ll3 = LinkedList.from_value_list([9, 8, 321, 123, 333])
    ll4 = LinkedList.from_value_list([9, 8, 321, 4, 4, 56])

    assert is_intersection_suboptimal(ll3, ll4) == (False, None)
    assert is_intersection(ll3, ll4) == (False, None)

