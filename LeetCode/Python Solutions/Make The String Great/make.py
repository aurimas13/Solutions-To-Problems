class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for char in s:
            # Check if the current and last character in the stack form a bad pair
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
