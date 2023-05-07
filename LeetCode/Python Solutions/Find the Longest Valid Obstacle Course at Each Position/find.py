from bisect import bisect_left
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # Initialize the result list and a list to keep track of the subproblems
        result, tails = [], []

        # Iterate through each obstacle
        for obstacle in obstacles:
            # Find the position where the obstacle should be inserted
            index = bisect_left(tails, obstacle + 1)

            # If the index is equal to the length of tails, it means we can extend the current subsequence
            if index == len(tails):
                tails.append(obstacle)
            # Otherwise, update the tails list with the current obstacle
            else:
                tails[index] = obstacle

            # Add the index + 1 to the result list
            result.append(index + 1)

        return result


if __name__ == '__main__':
    solution = Solution()

    # Test case 1
    test_obstacles_1 = [1, 2, 3, 2]
    expected_result_1 = [1, 2, 3, 3]
    assert solution.longestObstacleCourseAtEachPosition(test_obstacles_1) == expected_result_1

    # Test case 2
    test_obstacles_2 = [2, 2, 1]
    expected_result_2 = [1, 2, 1]
    assert solution.longestObstacleCourseAtEachPosition(test_obstacles_2) == expected_result_2

    # Test case 3
    test_obstacles_3 = [3, 1, 5, 1, 2, 4, 6]
    expected_result_3 = [1, 1, 2, 2, 3, 4, 5]
    assert solution.longestObstacleCourseAtEachPosition(test_obstacles_3) == expected_result_3

    print("All tests passed!")
