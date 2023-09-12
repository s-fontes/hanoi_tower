from typing import List


class Stack:
    items: List[int]

    def __init__(self) -> None:
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self) -> int:
        try:
            return self.items[-1]
        except IndexError:
            return 0

    def size(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)
