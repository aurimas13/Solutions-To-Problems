from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        operations = 0

        for count in freq.values():
            # If exactly one occurrence, impossible to remove it
            if count == 1:
                return -1
            
            # 'Three elements removal' operations
            operations += count // 3
            
            # If there's a remainder, one more operation is needed
            if count % 3:
                operations += 1
                
        return operations
