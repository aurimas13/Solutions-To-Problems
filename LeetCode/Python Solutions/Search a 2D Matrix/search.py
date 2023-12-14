from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row: List[int]) -> bool:
            """Perform binary search for the target within a row."""
            left, right = 0, len(row) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        # Iterate through each row in the matrix.
        for row in matrix:
            # If target is within the first and last element of the row, perform binary search.
            if row[0] <= target <= row[-1]:
                if binary_search(row):
                    return True

        return False


if __name__ == "__main__":
    s = Solution()

    # Test cases
    test_cases = [
        ({"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 3}, True),
        ({"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], "target": 13}, False),
        ({"matrix": [[1]], "target": 1}, True),
        ({"matrix": [[1]], "target": 2}, False)
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.searchMatrix(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
