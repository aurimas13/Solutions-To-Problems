class NestedIterator:
    def __init__(self, nestedList):
        # Initialize the stack with the reversed input to maintain order.
        self.stack = nestedList[::-1]

    def next(self) -> int:
        # Since 'hasNext' ensures the top of the stack is an integer, we can safely pop the stack and get the integer.
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        # Check the top of the stack. If it's a list, we need to further unwrap it.
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True  # The top of the stack is an integer, ready for 'next'.
            self.stack.pop()  # The top is a list, pop and process it.
            # Extend the stack with the reversed list for correct order.
            self.stack.extend(top.getList()[::-1])
        return False  # Stack is empty; no more integers left.