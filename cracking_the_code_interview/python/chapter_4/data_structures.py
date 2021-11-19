from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    value: Any
    adjacent_nodes: list["Node"]


@dataclass
class Graph:
    nodes: list[Node]

    def add(self, n: Node):
        self.nodes.append(n)


@dataclass
class TreeNode:
    value: Any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None
