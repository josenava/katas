from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


@dataclass
class Queue:
    first: Optional[Node] = None
    last: Optional[Node] = None

    def add(self, item: Any) -> None:
        n = Node(item)
        if self.last is None:
            self.last.next = n
        self.last = n

        if self.first is None:
            self.first = self.last

    def remove(self) -> Any:
        if self.first is None:
            raise ValueError("Empty Queue")
        value = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = self.first

        return value

    def peek(self) -> Any:
        if self.first is None:
            raise ValueError("Empty Queue")
        return self.first.data

    def is_empty(self) -> bool:
        return self.first is None

    def __repr__(self) -> str:
        if self.first is None:
            return "Empty queue"
        queue_str = "Queue(F|{queue}|L)"
        queue = ""
        aux = self.first
        while aux is not None:
            queue += f"{str(aux.data)}<-"

        return queue_str.format(queue=queue)
