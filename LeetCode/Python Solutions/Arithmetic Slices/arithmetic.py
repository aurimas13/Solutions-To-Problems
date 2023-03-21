from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        dp = [0] * len(nums)
        result = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                result += dp[i]

        return result

# Test cases
def test_solution():
    solution = Solution()
    assert solution.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert solution.numberOfArithmeticSlices([1, 3, 5, 7, 9]) == 6
    assert solution.numberOfArithmeticSlices([1, 1, 2, 5, 7]) == 0
    assert solution.numberOfArithmeticSlices([1, 2, 3, 5, 7, 9]) == 4
    assert solution.numberOfArithmeticSlices([]) == 0
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()
