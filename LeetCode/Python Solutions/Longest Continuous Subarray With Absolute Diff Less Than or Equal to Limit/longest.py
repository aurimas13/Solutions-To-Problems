from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        left = 0
        result = 0

        for right in range(len(nums)):
            while maxDeque and nums[maxDeque[-1]] <= nums[right]:
                maxDeque.pop()
            while minDeque and nums[minDeque[-1]] >= nums[right]:
                minDeque.pop()
            
            maxDeque.append(right)
            minDeque.append(right)
            
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                left += 1
                if maxDeque[0] < left:
                    maxDeque.popleft()
                if minDeque[0] < left:
                    minDeque.popleft()
            
            result = max(result, right - left + 1)
        
        return result

# Example usage:
sol = Solution()
print(sol.longestSubarray([8,2,4,7], 4))  # Output: 2
print(sol.longestSubarray([10,1,2,4,7,2], 5))  # Output: 4
print(sol.longestSubarray([4,2,2,2,4,4,2,2], 0))  # Output: 3
