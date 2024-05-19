from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] * n
        total_sum = sum(nums)
        
        # Calculate the difference when XOR is applied
        for i in range(n):
            diff[i] = (nums[i] ^ k) - nums[i]
        
        # Sort the differences in descending order
        diff.sort(reverse=True)
        
        # Sum the pairs of the differences
        for i in range(0, n, 2):
            if i + 1 == n:
                return total_sum
            pair_sum = diff[i] + diff[i + 1]
            if pair_sum > 0:
                total_sum += pair_sum
        
        return total_sum

# Example usage
sol = Solution()
nums = [24, 78, 1, 97, 44]
k = 6
edges = [[0, 2], [1, 2], [4, 2], [3, 4]]
print(sol.maximumValueSum(nums, k, edges))  # Expected output: 260
