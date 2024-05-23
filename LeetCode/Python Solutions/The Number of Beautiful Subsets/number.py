from typing import List

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(start: int, current: List[int]) -> int:
            if start == len(nums):
                return 1 if current else 0
            count = 0
            count += backtrack(start + 1, current)  # Skip current element
            if not any(abs(current_val - nums[start]) == k for current_val in current):
                current.append(nums[start])
                count += backtrack(start + 1, current)
                current.pop()
            return count
        
        return backtrack(0, [])  # Start counting from empty subset

# Example usage
sol = Solution()
print(sol.beautifulSubsets([2, 4, 6], 2))  # Output: 4
print(sol.beautifulSubsets([1], 1))        # Output: 1
