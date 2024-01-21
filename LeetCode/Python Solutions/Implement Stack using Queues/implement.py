from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()  # Primary queue
        self.q2 = deque()  # Secondary queue

    def push(self, x: int) -> None:
        # Add the element to q2
        self.q2.append(x)
        
        # Transfer all the elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1

