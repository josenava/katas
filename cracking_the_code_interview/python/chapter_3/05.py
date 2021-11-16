from dataclasses import dataclass
from typing import Any, Optional

from chapter_3.stack import Node, Stack


@dataclass()
class SortedStack:
    tmp_stack: Stack
    top: Optional[Node] = None

    def push(self, item: Any):
        node = Node(item)
        if self.top is None:
            node.next = self.top
            self.top = node
        else:
            value = self.peek()
            while value <= node.data:
                self.pop()
                self.tmp_stack.push(value)
                if not self.is_empty():
                    value = self.peek()
                else:
                    break
            node.next = self.top
            self.top = node
            while not self.tmp_stack.is_empty():
                value = self.tmp_stack.pop()
                n = Node(value)
                n.next = self.top
                self.top = n

    def pop(self) -> Any:
        if self.top is None:
            raise ValueError("Empty stack")
        value = self.top.data
        self.top = self.top.next

        return value

    def peek(self) -> Any:
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
            aux = aux.next

        return f"Stack({stack_value})"


def sort_stack(s: Stack) -> None:
    tmp_stack: Stack = Stack()
    while not s.is_empty():
        tmp = s.pop()
        while not tmp_stack.is_empty() and tmp_stack.peek() > tmp:
            s.push(tmp_stack.pop())

        tmp_stack.push(tmp)
    while not tmp_stack.is_empty():
        s.push(tmp_stack.pop())


if __name__ == "__main__":
    s1 = Stack()
    s1.push(5)
    s1.push(8)
    s1.push(9)
    s1.push(1)
    s1.push(100)
    s1.push(3)

    sort_stack(s1)
    assert str(s1) == "Stack(|<-1<-3<-5<-8<-9<-100)"
