Problem description of "Unique Paths" can be found [here](https://leetcode.com/problems/unique-paths/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Unique%20Paths/unique.java).

**Explanation**:

1. We use dynamic programming to solve this problem. The idea is to calculate the number of unique paths to reach each cell in the grid.
2. For any cell (i, j), the number of unique paths to reach it is the sum of the number of paths to reach the cell above it (i-1, j) and the cell to its left (i, j-1).
3. We initialize the first row and first column with 1, as there's only one way to reach any cell in the first row (by moving right) or the first column (by moving down).
4. The final answer is the number of unique paths to reach the bottom-right corner, which is stored in dp[m-1][n-1].