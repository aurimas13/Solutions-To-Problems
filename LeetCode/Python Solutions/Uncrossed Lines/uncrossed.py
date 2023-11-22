from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]

        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[-1][-1]
    
# Test Cases:
if __name__ == "__main__":
    
    assert Solution().maxUncrossedLines([1,4,2], [1,2,4]) == 2
    assert Solution().maxUncrossedLines([2,5,1,2,5], [10,5,2,1,5,2]) == 3
    assert Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]) == 2
    assert Solution().maxUncrossedLines([1,1,2,1,2], [1,3,2,3,1]) == 3
    assert Solution().maxUncrossedLines([1,1,3,5,3,3,5,5,1,1], [2,3,2,1,3,5,3,2,2,1]) == 5
    assert Solution().maxUncrossedLines([1,3,7,1,7,5], [1,9,2,5,1]) == 2
    print("All passed")