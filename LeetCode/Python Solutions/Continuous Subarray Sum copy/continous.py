from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  # To handle case where the subarray starts from index 0
        cumulative_sum = 0
        
        for i, num in enumerate(nums):
            cumulative_sum += num
            if k != 0:  # Avoid division by zero
                cumulative_sum %= k
            
            if cumulative_sum in remainder_map:
                if i - remainder_map[cumulative_sum] > 1:
                    return True
            else:
                remainder_map[cumulative_sum] = i
        
        return False

# Example usage:
sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))  # True
print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))  # True
print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13)) # False
