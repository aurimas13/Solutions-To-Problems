# Import List from typing module
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
     # Obtain the number of rows and columns in the input matrix
        num_rows, num_cols = len(strs), len(strs[0])

        # Initialize a list to store the length of the longest increasing subsequence for each column
        dp = [1] * num_cols

        # Iterate through the columns of the input matrix
        for j in range(num_cols):
            # Iterate through the previous columns
            for i in range(j):
                # Check if the current column is lexicographically greater than the previous column for all rows
                if all(strs[row][i] <= strs[row][j] for row in range(num_rows)):
                    # Update the length of the longest increasing subsequence for the current column
                    dp[j] = max(dp[j], dp[i] + 1)

        # Return the result
        return num_cols - max(dp)


# Checking in terminal/console:
if __name__ == '__main__':
    # Test cases
    solution = Solution()
    # Test case 1
    print(solution.minDeletionSize(["babca", "bbazb"]))  # Output: 3
    # Test case 2
    print(solution.minDeletionSize(["edcba"]))  # Output: 4
    # Test case 3
    print(solution.minDeletionSize(["ghi", "def", "abc"]))  # Output: 0
