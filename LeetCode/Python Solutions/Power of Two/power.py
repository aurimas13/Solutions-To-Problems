class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A number is a power of two if it is greater than 0 and the bitwise AND of n and n-1 is 0
        return n > 0 and (n & (n - 1)) == 0
