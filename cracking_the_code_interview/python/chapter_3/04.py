from dataclasses import dataclass
from typing import Any

from chapter_3.stack import Stack


@dataclass()
class MyQueue:
    stack: Stack
    tmp_stack: Stack

    def add(self, item: Any):
        self.stack.push(item)

    def remove(self) -> Any:
        while not self.stack.is_empty():
            tmp_item = self.stack.pop()
            self.tmp_stack.push(tmp_item)
        item = self.tmp_stack.pop()
        while not self.tmp_stack.is_empty():
            tmp_item = self.tmp_stack.pop()
            self.stack.push(tmp_item)

        return item

    def peek(self) -> Any:
        while not self.stack.is_empty():
            tmp_item = self.stack.pop()
            self.tmp_stack.push(tmp_item)
        item = self.tmp_stack.peek()
        while not self.tmp_stack.is_empty():
            tmp_item = self.tmp_stack.pop()
            self.stack.push(tmp_item)

        return item

    def is_empty(self) -> bool:
        return self.stack.is_empty()
