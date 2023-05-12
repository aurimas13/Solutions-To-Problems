from  typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        lengths = [0] * n  # lengths[i] = longest ending in nums[i]
        counts = [1] * n  # count[i] = number of longest ending in nums[i]
        
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < num:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = 1 + lengths[j]
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]
        
        longest = max(lengths)
        return sum(c for l, c in zip(lengths, counts) if l == longest)

    
# Tests:
if __name__ == '__main__':
    assert Solution().findNumberOfLIS([1,3,5,4,7]) == 2
    assert Solution().findNumberOfLIS([2,2,2,2,2]) == 5
    assert Solution().findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3
    print('All Passed!')


# Submission Result:
# 223/223 cases passed (180 ms)
# Your runtime beats 99.09 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)ß