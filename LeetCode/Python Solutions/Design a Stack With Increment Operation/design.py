class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []  # Renamed from 'increment' to 'inc'
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.stack) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k: int, val: int) -> None:
        i = min(k - 1, len(self.stack) - 1)
        if i >= 0:
            self.inc[i] += val