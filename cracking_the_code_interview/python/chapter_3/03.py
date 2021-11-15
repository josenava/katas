from dataclasses import dataclass, field
from typing import Any

from chapter_3.stack import Stack


class FullSizeStackError(Exception):
    pass


@dataclass
class FixedSizeStack(Stack):
    size: int = 0
    max_size: int = 50

    def is_full(self):
        return self.size == self.max_size

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FullSizeStackError()
        self.size += 1
        super().push(value)

    def pop(self) -> Any:
        value = super().pop()
        self.size -= 1

        return value


class SetOfStacks:
    def __init__(self, capacity: int = 5):
        self.stacks: list[FixedSizeStack] = [FixedSizeStack()]
        self.capacity = capacity

    def push(self, value: Any):
        if not self.stacks[len(self.stacks) - 1].is_full():
            self.stacks[len(self.stacks) - 1].push(value)
        else:
            if len(self.stacks) == self.capacity:
                raise ValueError("All stacks are already full")
            new_stack = FixedSizeStack()
            new_stack.push(value)
            self.stacks.append(new_stack)

    def pop(self) -> Any:
        return self.stacks[len(self.stacks) - 1].pop()

    def pop_at(self, index: int) -> Any:
        # TODO proper solution
        return self.stacks[index].pop()
