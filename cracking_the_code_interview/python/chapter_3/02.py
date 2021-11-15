from typing import Any

from chapter_3.stack import Stack


class StackMin(Stack):
    def push(self, value: Any) -> None:
        peek = self.peek()
        if value <= peek[1]:
            min_value = value
        else:
            min_value = peek[1]

        super().push((value, min_value))

    def min(self) -> int:
        peek = self.peek()

        return peek[1]

    def pop(self) -> int:
        value = super().pop()[0]

        return value
