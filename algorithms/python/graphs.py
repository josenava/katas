from typing import Any, Union, Optional
from collections import defaultdict, deque


Value = Union[str, int]


class Vertex:
    def __init__(self, value: Value):
        self.value = value
        self.adjacent_vertices = []

    def add_adjacent_vertex(self, vertex: "Vertex"):
        """undirected graph, so each vertex adds each other"""
        if vertex in self.adjacent_vertices:
            return

        self.adjacent_vertices.append(vertex)
        vertex.add_adjacent_vertex(self)

    def __eq__(self, other: "Vertex") -> bool:
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)


def dfs_traverse(vertex: Vertex, visited_vertices: defaultdict[Any, bool]):
    visited_vertices[vertex.value] = True

    print(f"Visiting {vertex.value}")

    for v in vertex.adjacent_vertices:
        if visited_vertices[v.value]:
            continue
        dfs_traverse(v, visited_vertices)


def dfs(vertex: Vertex, search_value: Value, visited_vertices: defaultdict[Any, bool]) -> Optional[Vertex]:
    if vertex.value == search_value:
        return vertex

    visited_vertices[vertex.value] = True
    print(f"visiting {vertex.value}")

    for v in vertex.adjacent_vertices:
        if visited_vertices[v.value]:
            continue
        if v.value == search_value:
            return v

        expected_vertex = dfs(v, search_value, visited_vertices)
        if expected_vertex is not None:
            return expected_vertex

    return None


def bfs_traverse(vertex: Vertex):
    queue = deque()
    visited_vertices = defaultdict(bool)

    queue.append(vertex)
    visited_vertices[vertex.value] = True

    while len(queue) > 0:
        current_vertex = queue.popleft()
        print(f"visited {current_vertex.value}")

        for v in current_vertex.adjacent_vertices:
            if visited_vertices[v.value]:
                continue
            queue.append(v)
            visited_vertices[v.value] = True

def bfs(vertex: Vertex, search_value: Value) -> Optional[Vertex]:
    if vertex.value == search_value:
        return vertex

    queue = deque()
    visited_vertices = defaultdict(bool)

    visited_vertices[vertex.value] = True
    queue.append(vertex)

    while len(queue) > 0:
        current_vertex = queue.popleft()
        for v in current_vertex.adjacent_vertices:
            if visited_vertices[v.value]:
                continue
            if v.value == search_value:
                return v
            queue.append(v)
            visited_vertices[v.value] = True
    return None


if __name__ == "__main__":
    alice = Vertex("Alice")
    bob = Vertex("Bob")
    fred = Vertex("Fred")
    helen = Vertex("Helen")
    candy = Vertex("Candy")
    derek = Vertex("Derek")
    gina = Vertex("Gina")
    irena = Vertex("Irena")
    elaine = Vertex("Elaine")

    alice.add_adjacent_vertex(bob)
    alice.add_adjacent_vertex(candy)
    alice.add_adjacent_vertex(derek)
    alice.add_adjacent_vertex(elaine)

    bob.add_adjacent_vertex(fred)
    fred.add_adjacent_vertex(helen)
    helen.add_adjacent_vertex(candy)

    derek.add_adjacent_vertex(gina)
    derek.add_adjacent_vertex(elaine)
    gina.add_adjacent_vertex(irena)

    # test dfs
    print("testing dfs")
    visited_vertices = defaultdict(bool)
    dfs_traverse(alice, visited_vertices)

    visited_vertices = defaultdict(bool)
    search_value = "Irena"
    v = dfs(alice, search_value, visited_vertices)

    if v is None:
        print(f"could not find {search_value}")
    else:
        print(f"found {v.value}")

    # test bfs
    print("testing bfs")
    bfs_traverse(alice)
    search_value = "Irena"
    v_bfs = bfs(alice, search_value)
    if v_bfs is None:
        print(f"could not find {search_value}")
    else:
        print(f"found {v_bfs.value}")

    # jose example
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")

    a.add_adjacent_vertex(b)
    a.add_adjacent_vertex(c)
    b.add_adjacent_vertex(e)
    e.add_adjacent_vertex(g)

    c.add_adjacent_vertex(d)
    c.add_adjacent_vertex(f)

    visited_vertices = defaultdict(bool)
    print("dfs_traverse")
    dfs_traverse(a, visited_vertices)
    print("bfs_traverse")
    bfs_traverse(a)
