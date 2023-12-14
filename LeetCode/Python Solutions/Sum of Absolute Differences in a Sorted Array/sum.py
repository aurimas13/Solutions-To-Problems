from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        # Precompute the sum of all elements in the array
        total_sum = sum(nums)

        # Sum of elements on the left of the current element
        left_sum = 0

        for i in range(n):
            # Sum of elements on the right of the current element
            right_sum = total_sum - left_sum - nums[i]

            # Sum of absolute differences for the left and right parts
            result[i] = i * nums[i] - left_sum + right_sum - (n - i - 1) * nums[i]

            # Update the left sum for the next iteration
            left_sum += nums[i]

        return result
