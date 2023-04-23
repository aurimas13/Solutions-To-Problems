from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers for binary search.
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # If the target is found, return its index.
            if nums[mid] == target:
                return mid

            # If the left half of the array is sorted.
            if nums[left] <= nums[mid]:
                # If target is in the sorted left half, search there.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Else, the right half of the array is sorted.
            else:
                # If target is in the sorted right half, search there.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # If target is not found, return -1.
        return -1


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"nums": [4, 5, 6, 7, 0, 1, 2], "target": 0}, 4),
        ({"nums": [4, 5, 6, 7, 0, 1, 2], "target": 3}, -1),
        ({"nums": [1], "target": 0}, -1),
        ({"nums": [1], "target": 1}, 0)
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.search(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
