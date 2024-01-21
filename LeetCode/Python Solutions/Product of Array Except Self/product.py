from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = suffix = 1
        for i, _ in enumerate(nums):
            answer[i] *= prefix
            answer[-i - 1] *= suffix
            prefix *= nums[i]
            suffix *= nums[-i - 1]

        return answer


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.productExceptSelf(nums = [1,2,3,4])  # nums = [1,2,3,4] -> [24,12,8,6] | [-1,1,0,-3,3] -> [0,0,9,0,0]
    print(Solve)