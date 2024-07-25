from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Count the frequency of each number
        freq = Counter(nums)
        # Sort by frequency first (ascending) and then by value (descending)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums

# Example usage:
sol = Solution()
print(sol.frequencySort([1,1,2,2,2,3]))  # Output: [3, 1, 1, 2, 2, 2]
print(sol.frequencySort([2,3,1,3,2]))    # Output: [1, 3, 3, 2, 2]
print(sol.frequencySort([-1,1,-6,4,5,-6,1,4,1]))  # Output: [5, -1, 4, 4, -6, -6, 1, 1, 1]
