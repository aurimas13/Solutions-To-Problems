class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until finding the matching '('
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                # Pop the '(' from the stack
                stack.pop()
                # Push the reversed string back to the stack
                stack.extend(temp)
            else:
                # Push the current character to the stack
                stack.append(char)
        
        return ''.join(stack)
