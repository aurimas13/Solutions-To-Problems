from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = 0
        flipped = [0] * n
        flips_count = 0

        for i in range(n):
            if i >= k:
                flip ^= flipped[i - k]
            if nums[i] == flip:
                if i + k > n:
                    return -1
                flip ^= 1
                flipped[i] = 1
                flips_count += 1
        
        return flips_count

# Example usage
sol = Solution()
print(sol.minKBitFlips([0,1,0], 1))  # Output: 2
print(sol.minKBitFlips([1,1,0], 2))  # Output: -1
print(sol.minKBitFlips([0,0,0,1,0,1,1,0], 3))  # Output: 3
