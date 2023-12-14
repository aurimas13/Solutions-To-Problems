from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped = popped[1:]
        return len(stack)==0


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]) #pushed = [1,2,3,4,5], popped = [4,5,3,2,1] -> True | pushed = [1,2,3,4,5], popped = [4,3,5,1,2] -> False
    print(Solve)
