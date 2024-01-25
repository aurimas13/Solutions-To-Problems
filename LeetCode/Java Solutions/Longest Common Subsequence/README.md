Problem description of "Longest Common Subsequence" can be found [here](https://leetcode.com/problems/longest-common-subsequence/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Longest%20Common%20Subsequence/longest.java).

## Implementation

This Python solution efficiently computes the longest common subsequence between two strings using a space-optimized dynamic programming approach. It iteratively updates a single-dimensional array to store the longest common subsequence (LCS) lengths, significantly reducing space usage compared to a 2D array. The algorithm reverses the strings to facilitate the in-place update of the DP array, ensuring the accurate calculation of the LCS length while maintaining lower space complexity. The time complexity of the implementation is quadratic, and the space complexity is linear with respect to the length of the shorter input string.
