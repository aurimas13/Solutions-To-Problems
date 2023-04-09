class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Initialize the result to 0
        result = 0
        
        # Iterate while n is greater than 0
        while n > 0:
            # Update the result with XOR operation between the result and n
            result ^= n
            # Right shift n by 1 bit
            n >>= 1
        
        return result
