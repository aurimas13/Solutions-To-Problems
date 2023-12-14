from typing import List
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if (sum < k):
                answer = max(answer, sum)
                left += 1
            else:
                right -= 1
        return answer


# Checking in PyCharm console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.twoSumLessThanK(nums = [34, 23, 1, 24, 75, 33, 54, 8], k = 60)  # output: 58
    print(Solve)
