from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Initialize the maximum score, left pointer, and right pointer
        max_score = curr_min = nums[k]
        left, right = k, k

        # Iterate until the left and right pointers reach the ends of the array
        while left > 0 or right < len(nums) - 1:
            # Choose the direction to move (left or right)
            if left == 0:
                right += 1
            elif right == len(nums) - 1:
                left -= 1
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
            else:
                right += 1

            # Update the current minimum element and maximum score
            curr_min = min(curr_min, nums[left], nums[right])
            max_score = max(max_score, curr_min * (right - left + 1))

        return max_score


# Checking in terminal/console:
if __name__ == '__main__':
    # Test cases
    solution = Solution()

    # Test case 1
    print(solution.maximumScore([1, 4, 3, 7, 4, 5], 3))  # Output: 15
    # Test case 2
    print(solution.maximumScore([5, 5, 4, 5, 4, 1, 1, 1], 0))  # Output: 20
    # Test case 3
    print(solution.maximumScore([5, 5, 4, 1, 4, 1, 1, 1], 3))  # Output: 16
