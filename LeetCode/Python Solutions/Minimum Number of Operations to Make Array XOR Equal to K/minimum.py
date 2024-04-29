from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Calculate the initial XOR of all numbers
        currentXor = 0
        for num in nums:
            currentXor ^= num
        
        # Calculate the required XOR to make the XOR of the array equal to k
        requiredXor = currentXor ^ k
        
        # The number of operations needed is the number of 1's in the binary representation of requiredXor
        return bin(requiredXor).count('1')
