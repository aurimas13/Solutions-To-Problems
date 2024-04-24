class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        
        # Initialize base cases
        a, b, c = 0, 1, 1
        # Compute tribonacci starting from T_3
        for i in range(3, n + 1):
            # Compute the next number in the sequence
            next_value = a + b + c
            # Slide the window
            a, b, c = b, c, next_value
        
        return c
