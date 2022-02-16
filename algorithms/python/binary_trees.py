from dataclasses import dataclass
from typing import Union, Optional


Value = Union[str, int]


@dataclass
class TreeNode:
    value: Value
    left_child: Optional["TreeNode"] = None
    right_child: Optional["TreeNode"] = None

    def add_left(self, child: "TreeNode"):
        self.left_child = child

    def add_right(self, child: "TreeNode"):
        self.right_child = child


def search(root: TreeNode, value: Value) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.value == value:
        return root
    if value < root.value:
        return search(root.left_child, value)
    if value > root.value:
        return search(root.right_child, value)


def inorder_traverse(root: TreeNode):
    if root is None:
        return
    inorder_traverse(root.left_child)
    print(root.value)
    inorder_traverse(root.right_child)


def preorder_traverse(root: TreeNode):
    if root is None:
        return
    print(root.value)
    preorder_traverse(root.left_child)
    preorder_traverse(root.right_child)


def postorder_traverse(root: TreeNode):
    if root is None:
        return
    postorder_traverse(root.left_child)
    postorder_traverse(root.right_child)
    print(root.value)



if __name__ == "__main__":
    root = TreeNode(50)
    node1 = TreeNode(
        25, TreeNode(10, TreeNode(4), TreeNode(11)),
        TreeNode(33, TreeNode(30), TreeNode(40))
    )
    node2 = TreeNode(
        75, TreeNode(56, TreeNode(52), TreeNode(61)),
        TreeNode(89, TreeNode(82), TreeNode(95))
    )
    root.add_left(node1)
    root.add_right(node2)

    search_value = 109
    node = search(root, search_value)
    if node is None:
        print(f"could not find {search_value}")
    else:
        print(f"{search_value} found")

    print("INorder traverse")
    inorder_traverse(root)
    print("PREorder traverse")
    preorder_traverse(root)
    print("POSTorder traverse")
    postorder_traverse(root)
