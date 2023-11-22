from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Check if k is less than or equal to 1
        if k <= 1:
            return 0

        # Initialize the product, left pointer, and the result count
        prod = 1
        left = 0
        count = 0

        # Iterate through the nums list with a right pointer
        for right, val in enumerate(nums):
            # Update the product by multiplying it with the current value
            prod *= val

            # Move the left pointer to the right and divide the product by the nums[left] until the product is less than k
            while prod >= k:
                prod /= nums[left]
                left += 1

            # Update the count by adding the length of the current subarray
            count += right - left + 1

        return count

# Test cases to run in the terminal/console
if __name__ == "__main__":
    s = Solution()

    assert s.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
    assert s.numSubarrayProductLessThanK([1, 1, 1], 1) == 0
    assert s.numSubarrayProductLessThanK([1, 1, 1], 2) == 6
    assert s.numSubarrayProductLessThanK([1, 2, 3], 0) == 0
