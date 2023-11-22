class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: when n is zero, result is always 1 
        if n == 0:
            return 1.0

        # if n is negative, change the problem to x^-n to 1/x^n
        if n < 0:
            return self.myPow(1/x, -n)

        # Recursive case
        else:
            half = self.myPow(x, n // 2)  # Calculate power of half n
            
            # If n is even, the result is half*half
            if n % 2 == 0:
                return half * half
            # If n is odd, the result is half*half*x
            else:
                return half * half * x
