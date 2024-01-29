class MyQueue:

    def __init__(self):
        self.stack1 = []  # Stack for enqueue
        self.stack2 = []  # Stack for dequeue

    def push(self, x: int) -> None:
        self.stack1.append(x)  # Push element onto the stack1

    def pop(self) -> int:
        self.move()
        return self.stack2.pop()  # Pop element from stack2

    def peek(self) -> int:
        self.move()
        return self.stack2[-1]  # Peek element from stack2

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)  # Check if both stacks are empty

    def move(self) -> None:
        if not self.stack2:  # Move elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
