from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array with size n+1 and first element as 0
        res = [0] * (n + 1)
        
        # Loop from 1 to n to compute the number of 1's for each number
        for i in range(1, n + 1):
            # If i is even, number of 1's is same as number of 1's in i/2
            # If i is odd, number of 1's is number of 1's in i-1 plus 1
            res[i] = res[i >> 1] + (i & 1)
        
        return res
