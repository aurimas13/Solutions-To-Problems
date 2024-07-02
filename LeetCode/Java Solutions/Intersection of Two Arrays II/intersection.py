from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find the intersection of both counters
        intersection = count1 & count2
        
        # Convert the intersection to a list of elements
        result = []
        for num in intersection.elements():
            result.append(num)
        
        return result

# Example usage:
sol = Solution()
print(sol.intersect([1, 2, 2, 1], [2, 2]))  # Output: [2, 2]
print(sol.intersect([4, 9, 5], [9, 4, 9, 8, 4]))  # Output: [4, 9]
