from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Remove duplicates and sort the array
        sorted_nums = sorted(list(set(nums)))

        # Use two pointers to represent a sliding window over the sorted array
        l, r = 0, 0
        n = len(nums)
        max_count = 0

        # Slide the window
        while r < len(sorted_nums):
            # If the window is too large, reduce it from the left
            while sorted_nums[r] - sorted_nums[l] >= n:
                l += 1
            max_count = max(max_count, r - l + 1)
            r += 1

        # Return the number of operations required
        return n - max_count

# Test cases
s = Solution()
print(s.minOperations([4,2,5,3]))  # 0
print(s.minOperations([1,2,3,5,6]))  # 1
print(s.minOperations([1,10,100,1000]))  # 3
