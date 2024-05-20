from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index, current_xor):
            # If we've considered all elements, add the current XOR to the total sum
            if index == len(nums):
                return current_xor
            # Recursively calculate the XOR sum including the current element
            include = backtrack(index + 1, current_xor ^ nums[index])
            # Recursively calculate the XOR sum excluding the current element
            exclude = backtrack(index + 1, current_xor)
            # Return the sum of both choices
            return include + exclude
        
        # Start backtracking from index 0 with an initial XOR value of 0
        return backtrack(0, 0)

# Example usage
sol = Solution()
print(sol.subsetXORSum([1, 3]))  # Output: 6
print(sol.subsetXORSum([5, 1, 6]))  # Output: 28
print(sol.subsetXORSum([3, 4, 5, 6, 7, 8]))  # Output: 480
