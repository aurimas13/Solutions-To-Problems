from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height) - 1, 0

        # Continue until pointers meet
        while l < r:
            # Calculate the area between the two heights and update the max area
            max_area = max((r - l) * min(height[l], height[r]), max_area)

            # Move the pointer with the smaller height inwards
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

if __name__ == '__main__':
    s = Solution()

    # Test cases
    test_cases = [
        ({"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, 49),
        ({"height": [1, 1]}, 1),
        ({"height": [4, 3, 2, 1, 4]}, 16),
        ({"height": [1, 2, 1]}, 2)
    ]

    for i, (test_input, expected_output) in enumerate(test_cases):
        result = s.maxArea(**test_input)
        assert result == expected_output, f"Test case {i} failed: expected {expected_output}, got {result}"
        print(f"Test case {i} succeeded")
