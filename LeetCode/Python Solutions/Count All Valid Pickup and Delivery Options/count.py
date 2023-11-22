class Solution:
    def countOrders(self, n: int) -> int:
        # Define the modulo constant
        MOD = 10**9 + 7
        
        # Initialize the result to 1
        res = 1
        
        # Calculate the result using the formula
        for i in range(1, n + 1):
            res = (res * i * (2*i - 1)) % MOD
        
        return res

