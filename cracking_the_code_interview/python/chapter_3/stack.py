from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


@dataclass
class Stack:
    top: Optional[Node] = None

    def pop(self) -> Any:
        if self.top is None:
            raise ValueError("Stack is empty")
        value = self.top.data
        self.top = self.top.next

        return value

    def push(self, value: Any) -> None:
        n = Node(value)
        n.next = self.top
        self.top = n

    def peek(self) -> Any:
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None

    def __repr__(self) -> str:
        if self.top is None:
            return "Empty Stack"
        aux = self.top
        stack_value = "|"
        while aux is not None:
            stack_value += f"<-{str(aux.data)}"

        return f"Stack({stack_value})"
