from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 1:
            return True

        last_position = N - 1  # Initialize the last position as the last index in the nums list

        # Iterate backwards through the nums list
        for i in range(N - 2, -1, -1):
            # Check if the current element can reach or pass the last_position
            if nums[i] + i >= last_position:
                last_position = i  # Update the last_position to the current index

        # If the last_position is 0, then it is possible to reach the last index
        return last_position == 0


# Checking in terminal/console:
if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0, 1], False),
        ([1, 2, 3, 4], True),
    ]
    for nums, expected in test_cases:
        result = sol.canJump(nums)
        print(f"Input: {nums}, Output: {result}, Expected: {expected}, Result: {result == expected}")from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        if N < 1:
            return True

        last_position = N - 1  # Initialize the last position as the last index in the nums list

        # Iterate backwards through the nums list
        for i in range(N - 2, -1, -1):
            # Check if the current element can reach or pass the last_position
            if nums[i] + i >= last_position:
                last_position = i  # Update the last_position to the current index

        # If the last_position is 0, then it is possible to reach the last index
        return last_position == 0


# Checking in terminal/console:
if __name__ == '__main__':
    sol = Solution()
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([1, 0, 1], False),
        ([1, 2, 3, 4], True),
    ]
    for nums, expected in test_cases:
        result = sol.canJump(nums)
        print(f"Input: {nums}, Output: {result}, Expected: {expected}, Result: {result == expected}")