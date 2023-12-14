from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Perform binary search to find the peak element.
        while left < right:
            mid = left + (right - left) // 2

            # If the current element is less than the next element,
            # the peak element is in the right half.
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"nums": [1, 2, 3, 1]}, 2),
        ({"nums": [1, 2, 1, 3, 5, 6, 4]}, 5),
        ({"nums": [1]}, 0),
        ({"nums": [1, 2]}, 1),
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.findPeakElement(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
