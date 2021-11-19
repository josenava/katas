from typing import Optional

from chapter_4.data_structures import TreeNode


def build_minimal_height_bst(values: list[int], start_index: int, end_index: int) -> Optional[TreeNode]:
    if end_index < start_index:
        return None

    mid_index = (end_index + start_index) // 2
    tree_node = TreeNode(values[mid_index])
    tree_node.left = build_minimal_height_bst(values, start_index, mid_index-1)
    tree_node.right = build_minimal_height_bst(values, mid_index+1, end_index)

    return tree_node


def build_minimal_height_bst_from_sorted_list(values: list[int]) -> TreeNode:
    return build_minimal_height_bst(values, 0, len(values) - 1)


if __name__ == "__main__":
    sorted_values = [1, 2, 65, 98, 300, 534, 2222, 39238]
    t = build_minimal_height_bst_from_sorted_list(sorted_values)

    print(t)
