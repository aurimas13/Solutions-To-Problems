from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        if len(nums1) == 0 or len(nums2) == 0:
            return []  # Return an empty list if either input list is empty
        
        nums1.sort()  # O(n1 * log(n1)) where n1 is the length of nums1
        nums2.sort()  # O(n2 * log(n2)) where n2 is the length of nums2
        
        # Using list comprehension and set difference, find elements in nums1 not in nums2
        # The time complexity for this step is O(n1 + n2)
        diff1 = list(set(nums1) - set(nums2))
        
        # Using list comprehension and set difference, find elements in nums2 not in nums1
        # The time complexity for this step is O(n1 + n2)
        diff2 = list(set(nums2) - set(nums1))
        
        return [diff1, diff2]  # Return the list containing diff1 and diff2


# Test
solution = Solution()
print(solution.findDifference([1, 2, 3, 3], [1, 1, 2, 2]))  # Should print [[3], []]