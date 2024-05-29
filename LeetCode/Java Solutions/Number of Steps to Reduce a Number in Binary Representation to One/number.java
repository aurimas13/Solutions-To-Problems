class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        
        # Start from the least significant bit and move to the most significant bit
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                # If the current bit + carry is 1, it's odd, so we need to add 1
                carry = 1  # This effectively becomes carry for the next higher bit
                steps += 2  # 1 for addition and 1 for division
            else:
                # If the current bit + carry is 0, it's even, so we just divide by 2
                steps += 1
        
        # If there's a carry after processing all bits except the leftmost one
        return steps + carry

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.numSteps("1101"))  # Output: 6
    print(sol.numSteps("10"))    # Output: 1
    print(sol.numSteps("1"))     # Output: 0
