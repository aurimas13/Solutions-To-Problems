The problem of "Perfect Squares" is found [here](https://leetcode.com/problems/perfect-squares/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Permutations/perfect.java).

To check the solution in terminal first compile Java file as `javac perfect.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The Java solution uses dynamic programming with an integer array `dp` to keep track of the minimum number of perfect square numbers for each value up to `n`. It iterates through each number, computing the minimum number of squares needed by examining all smaller square numbers. This approach ensures that the solution is computed in a bottom-up manner, utilizing previously computed results to find the minimum count for the current number.