from  typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
                    elif dp[i][0] < dp[j][0] + 1:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
        max_len = max([x[0] for x in dp])
        return sum([x[1] for x in dp if x[0] == max_len])
    
# Tests:
if __name__ == '__main__':
    assert Solution().findNumberOfLIS([1,3,5,4,7]) == 2
    assert Solution().findNumberOfLIS([2,2,2,2,2]) == 5
    assert Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3
    assert Solution().findNumberOfLIS([1,2,4,3,5,4,7,2,1,2,4,3,5,4,7,2]) == 3
    assert Solution().findNumberOfLIS([1,2,4,3,5,4,7,2,1,2,4,3,5,4,7,2,1,2,4,3,5,4,7,2]) == 3   

print('All Passed!')

# Submission Result:
# 223/223 cases passed (180 ms)
# Your runtime beats 99.09 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)ß