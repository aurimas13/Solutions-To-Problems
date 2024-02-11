The problem of "Cherry Pickup II" is found [here](https://leetcode.com/problems/cherry-pickup-ii/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Cherry%20Pickup%20II/cherry.java).

To check the solution in terminal first compile Java file as `javac cherry.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The solution implements a bottom-up dynamic programming approach to find the maximum number of cherries two robots can collect. It starts by initializing a DP table that stores the maximum cherries collected for any pair of column positions for each robot on each row. We then iterate through the grid from the bottom row to the top row, updating the DP table based on the possible moves of each robot.

For each cell (r, c1) for Robot #1 and (r, c2) for Robot #2, we consider all combinations of moves the robots can make from the next row (i.e., row r+1). This includes moving left, staying in place, or moving right, resulting in 9 combinations of moves for both robots. We calculate the maximum cherries that can be collected for each combination and update the DP table accordingly.

The key to this approach is recognizing that the maximum cherries collected up to row r depend only on the decisions made from row r+1 onwards, allowing us to use dynamic programming to avoid recalculating overlapping subproblems.
