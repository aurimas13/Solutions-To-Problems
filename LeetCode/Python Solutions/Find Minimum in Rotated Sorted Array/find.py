from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        # Perform binary search to find the minimum element.
        while nums[left] > nums[right]:
            mid = (left + right) // 2

            # If the middle element is less than the right element,
            # the minimum element is in the left half (including mid).
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"nums": [3, 4, 5, 1, 2]}, 1),
        ({"nums": [4, 5, 6, 7, 0, 1, 2]}, 0),
        ({"nums": [11, 13, 15, 17]}, 11),
        ({"nums": [2, 1]}, 1),
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.findMin(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
