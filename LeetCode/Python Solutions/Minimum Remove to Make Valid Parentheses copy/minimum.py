class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # First pass: Remove invalid closing parentheses
        balance, validString = 0, []
        for char in s:
            if char == '(':
                balance += 1
            elif char == ')':
                if balance == 0:
                    continue  # Skip this character
                balance -= 1
            validString.append(char)
        
        # Second pass: Remove invalid opening parentheses from the end
        result, openCount = [], 0
        for char in reversed(validString):
            if char == '(' and balance > 0:
                balance -= 1
                continue  # Skip this character
            result.append(char)
        
        return ''.join(reversed(result))
