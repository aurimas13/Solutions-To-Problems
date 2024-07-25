from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        # Append remaining elements, if any
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array

# Example usage:
sol = Solution()
print(sol.sortArray([5,2,3,1]))  # Output: [1,2,3,5]
print(sol.sortArray([5,1,1,2,0,0]))  # Output: [0,0,1,1,2,5]
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        sorted_array = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        
        # Append remaining elements, if any
        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])
        
        return sorted_array

# Example usage:
sol = Solution()
print(sol.sortArray([5,2,3,1]))  # Output: [1,2,3,5]
print(sol.sortArray([5,1,1,2,0,0]))  # Output: [0,0,1,1,2,5]
