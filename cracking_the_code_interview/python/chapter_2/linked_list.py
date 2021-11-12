from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


@dataclass
class LinkedList:
    head: Optional[Node] = None

    @classmethod
    def from_value_list(cls, values: list[int]) -> "LinkedList":
        ll = cls()
        for v in values:
            n = Node(v)
            ll.add(n)

        return ll

    def add(self, n: Node) -> None:
        n.next = self.head
        self.head = n

    def delete(self, value: int) -> None:
        aux = self.head
        prev = None
        if self.head.value == value:
            aux = aux.next
            self.head = aux
            return
        while aux is not None:
            if aux.value == value:
                break
            prev = aux
            aux = aux.next

        if aux is None:
            return

        prev.next = aux.next

        return

    def __repr__(self) -> str:
        aux = self.head
        str_list = ""
        while aux is not None:
            str_list += f"{aux.value}->"
            aux = aux.next

        return f"LinkedList({str_list})"

    def __eq__(self, other: "LinkedList") -> bool:
        aux = self.head
        other_aux = other.head

        while aux is not None and other_aux is not None:
            if aux.value != other_aux.value:
                return False
            aux = aux.next
            other_aux = other_aux.next

        if any(n is not None for n in [aux, other_aux]):
            return False

        return True

