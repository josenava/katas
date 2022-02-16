from typing import Optional

from chapter_2.linked_list import LinkedList, Node
from chapter_4.data_structures import TreeNode


def level_ll_items(item: TreeNode, lists: list[LinkedList], level: int) -> None:
    if item is None:
        return None

    if len(lists) == level:
        ll = LinkedList()
        lists.append(ll)
    else:
        ll = lists[level]

    ll.add(Node(item.value))
    level_ll_items(item.left, lists, level+1)
    level_ll_items(item.right, lists, level+1)


def ll_depth_items(root: TreeNode) -> list[LinkedList]:
    lists: list[LinkedList] = []
    level_ll_items(root, lists, 0)

    return lists


if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(
        5,
        TreeNode(2, None, TreeNode(3)),
        TreeNode(6)
    )

    root.right = TreeNode(9)

    lls = ll_depth_items(root)
    print(lls)
    assert len(lls) == 4
