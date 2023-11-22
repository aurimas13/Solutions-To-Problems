import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Find the logarithm of n with base 4
        log_n = math.log(n, 4)
        
        # Check if log_n is a whole number (or very close to it, considering floating-point precision)
        return math.isclose(log_n, round(log_n))
