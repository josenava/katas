from typing import Optional


class CustomArrayStack:
    def __init__(self, stack_capacity: int):
        self.stack_capacity = stack_capacity
        self.stacks_number = 3
        self.values: list[Optional[int]] = [None for _ in range(0, self.stack_capacity * self.stacks_number)]
        self.sizes = [0 for _ in range(0, self.stacks_number)]

    def _is_full(self, stack_n: int) -> bool:
        return self.sizes[stack_n] == self.stack_capacity

    def push(self, stack_n: int, value: int):
        if self._is_full(stack_n):
            raise ValueError("Stack is already full")

        self.sizes[stack_n] += 1
        self.values[self._top_index(stack_n)] = value

    def is_empty(self, stack_n: int) -> bool:
        return self.sizes[stack_n] == 0

    def pop(self, stack_n: int) -> int:
        if self.is_empty(stack_n):
            raise ValueError("Empty Stack")
        top_position = self._top_index(stack_n)
        value = self.values[top_position]
        self.values[top_position] = None
        self.sizes[stack_n] -= 1

        return value

    def peek(self, stack_n: int) -> int:
        if self.is_empty(stack_n):
            raise ValueError("Empty Stack")
        top_position = self._top_index(stack_n)
        value = self.values[top_position]

        return value

    def _top_index(self, stack_n: int) -> int:
        offset = self.stack_capacity * stack_n

        return offset + self.sizes[stack_n] - 1
