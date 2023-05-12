from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Calculate the max distance for ants on the left side
        max_left = max(left) if left else 0
        
        # Calculate the min position for ants on the right side and then its distance from the left end
        min_right = n - min(right) if right else 0
        
        # Return the max of max_left and min_right as the last moment before all ants fall
        return max(max_left, min_right)


# Test cases
def run_tests():
    solution = Solution()
    
    test_cases = [
        (4, [4, 3], [0, 1], 4),
        (7, [], [0, 1, 2, 3, 4, 5, 6, 7], 7),
        (9, [5, 3, 7], [2, 4, 6], 7),
        (6, [1, 3, 5], [], 5),
        (100, [50, 60], [30, 20, 10], 90),
    ]
    
    for i, (n, left, right, expected) in enumerate(test_cases):
        result = solution.getLastMoment(n, left, right)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} succeeded")

# Checking in Terminal
if __name__ == '__main__':
    run_tests()
