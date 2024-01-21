class MinStack:

    def __init__(self):
        self.array1 = []

    def push(self, val: int) -> None:
        self.array1.append(val)

    def pop(self) -> None:
        return self.array1.pop()

    def top(self) -> int:
        return self.array1[-1]

    def getMin(self) -> int:
        return min(self.array1)


# Instantiation of the class to check the values in PyCharm
if __name__ == '__main__':
    minStack = MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();
    minStack.pop();
    minStack.top();
    minStack.getMin();
    print(minStack)
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]] -> [None,None,None,None,-3,None,0,-2]
