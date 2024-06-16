from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        i = 0
        patches = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        
        return patches

# Example usage:
solution = Solution()
print(solution.minPatches([1, 3], 6))  # Output: 1
print(solution.minPatches([1, 5, 10], 20))  # Output: 2
print(solution.minPatches([1, 2, 2], 5))  # Output: 0
