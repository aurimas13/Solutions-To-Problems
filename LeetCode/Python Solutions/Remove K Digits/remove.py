class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # If k is still greater than 0, remove the last k digits
        final_stack = stack[:-k] if k else stack
        
        # Convert stack to string and strip leading zeros
        return ''.join(final_stack).lstrip('0') or "0"