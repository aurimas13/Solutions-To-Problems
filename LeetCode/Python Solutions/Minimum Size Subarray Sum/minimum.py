from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize variables
        left, right, curr_sum, min_length = 0, 0, 0, float('inf')

        # Iterate through nums with the right pointer
        while right < len(nums):
            # Add the current value to the running sum
            curr_sum += nums[right]

            # Check if the current sum is equal or greater than the target
            while curr_sum >= target:
                # Calculate the length of the current subarray
                curr_length = right - left + 1

                # Update the minimum length if the current length is smaller
                min_length = min(min_length, curr_length)

                # Remove the leftmost value from the running sum and move the left pointer
                curr_sum -= nums[left]
                left += 1

            # Move the right pointer
            right += 1

        # Return the minimum length or 0 if no subarray was found
        return min_length if min_length != float('inf') else 0


def test_solution():
    s = Solution()

    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert s.minSubArrayLen(100, []) == 0
    assert s.minSubArrayLen(3, [1, 1]) == 0


if __name__ == '__main__':
    test_solution()
