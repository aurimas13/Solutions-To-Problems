import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # Calculate the length of the nums
        n = len(nums)

        # Initialize the dp array with 0
        dp = [0] * (1 << n)
        gcd = [[0]*n for _ in range(n)]

        # Calculate the gcd for all pairs
        for i in range(n):
            for j in range(i+1, n):
                gcd[i][j] = math.gcd(nums[i], nums[j])

        # Dynamic programming to calculate the maxScore
        for mask in range(1, 1 << n):
            bits = [b for b in range(n) if ((mask >> b) & 1)]
            if len(bits) % 2 == 0:
                for i in range(len(bits)):
                    for j in range(i+1, len(bits)):
                        dp[mask] = max(dp[mask], dp[mask ^ (1 << bits[i]) ^ (1 << bits[j])] + (len(bits)//2) * gcd[bits[i]][bits[j]])
        return dp[-1]


if __name__ == "__main__":
    # Tests
    s = Solution()
    assert s.maxScore([1, 2]) == 1, "Test Case 1 Failed"
    assert s.maxScore([3, 4, 6, 8]) == 11, "Test Case 2 Failed"
    assert s.maxScore([1, 2, 3, 4, 5, 6]) == 14, "Test Case 3 Failed"
    print("All test cases passed!")
