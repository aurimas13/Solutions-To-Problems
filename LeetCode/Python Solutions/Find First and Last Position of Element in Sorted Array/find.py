from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize the result list with -1 as both the first and last position.
        res = [-1, -1]

        # Find the first occurrence of target using binary search.
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        res[0] = left

        # Find the last occurrence of target using binary search.
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        res[1] = right

        # Check if target was not found.
        if res[0] > res[1]:
            res = [-1, -1]

        return res


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"nums": [5, 7, 7, 8, 8, 10], "target": 8}, [3, 4]),
        ({"nums": [5, 7, 7, 8, 8, 10], "target": 6}, [-1, -1]),
        ({"nums": [], "target": 0}, [-1, -1]),
        ({"nums": [1], "target": 1}, [0, 0])
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.searchRange(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")

