from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)

        # Helper function to find the maximum sum of non-adjacent elements in a circular list
        def dp_helper(arr: List[int], num_slices: int) -> int:
            dp = [0] * (num_slices + 1)
            dp_prev = [0] * (num_slices + 1)

            # Update the dynamic programming table for each slice size
            for size in arr:
                new_dp = dp[:]
                for i in range(1, num_slices + 1):
                    new_dp[i] = max(dp[i], dp_prev[i - 1] + size)
                dp_prev, dp = dp, new_dp
            
            # Return the maximum sum of selected slices
            return dp[-1]

        # Case 1: Exclude first slice, include last slice
        case1 = dp_helper(slices[1:], n // 3)
        
        # Case 2: Exclude last slice, include first slice
        case2 = dp_helper(slices[:-1], n // 3)
        
        # Return the maximum sum of both cases
        return max(case1, case2)


# Running in terminal/console:
if __name__ == '__main__':
    slices = [1, 2, 3, 4, 5, 6]
    solution = Solution()
    Solve = solution.maxSizeSlices(slices)
    # Output: 10
    print(Solve)
