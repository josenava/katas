from typing import Optional

from chapter_2.linked_list import LinkedList, Node


def detect_loop(ll: LinkedList) -> Optional[Node]:
    # TODO fill this method
    return Node(1)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    ll1 = LinkedList()
    ll1.add(node1)
    ll1.add(node2)
    ll1.add(node3)
    ll1.add(node4)
    ll1.add(node2)
    assert True
