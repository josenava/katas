from collections import deque
from dataclasses import dataclass
from enum import IntEnum

from chapter_4.data_structures import Graph, Node


class NodeState(IntEnum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


@dataclass
class GNode(Node):
    state: NodeState = NodeState.UNVISITED


def route_exists(n1: GNode, n2: GNode) -> bool:
    q = deque()
    n1.state = NodeState.VISITING

    q.append(n1)
    while len(q) > 0:
        n = q.pop()
        for v in n.adjacent_nodes:
            if v.state == NodeState.UNVISITED:
                if v is n2:
                    return True
                else:
                    v.state = NodeState.VISITING
                    q.append(v)
        n.state = NodeState.VISITED

    return False


if __name__ == "__main__":
    node0 = GNode(0, [])
    node3 = GNode(3, [])
    node2 = GNode(2, [node3])
    node1 = GNode(1, [node0, node2])
    graph = Graph([node0, node1, node2, node3])

    assert route_exists(node1, node3)
