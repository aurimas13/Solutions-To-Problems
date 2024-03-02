class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Count the number of 1s and 0s
        ones = s.count('1')
        zeros = s.count('0')
        
        # Ensure at least one '1' is at the end to make it odd, adjust counts
        ones -= 1
        
        # The maximum odd binary number: all remaining '1's, followed by all '0's, ending with a '1'
        return '1' * ones + '0' * zeros + '1'
