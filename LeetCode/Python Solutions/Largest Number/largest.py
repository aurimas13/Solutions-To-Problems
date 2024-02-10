from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort nums to ensure that every element is divisible by its previous one if they are in the same subset
        nums.sort()
        n = len(nums)
        # dp[i] stores the size of the largest divisible subset that ends with nums[i]
        dp = [1] * n
        # prev[i] stores the previous index of nums[i] in the largest divisible subset that ends with nums[i]
        prev = [-1] * n
        max_size, max_idx = 1, 0
        
        # Build up dp and prev
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_size:
                        max_size, max_idx = dp[i], i
                        
        # Reconstruct the largest divisible subset
        subset = []
        while max_idx != -1:
            subset.append(nums[max_idx])
            max_idx = prev[max_idx]
        
        return subset[::-1]  # Return in ascending order
