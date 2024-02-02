The problem of "Sequential Digits" can be found [here](https://leetcode.com/problems/sequential-digits/description/) while the solution [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Python%20Solutions/Sequential%20Digits/sequential.py).

## Implementation

The solution generates all possible sequential digit numbers and then filter them based on the given range [low, high]. This approach is efficient because the total number of sequential digit numbers is limited and can be precomputed. Filtering based on the low and high range ensures that only valid numbers are included in the result. This method provides an efficient solution to the problem, avoiding unnecessary checks for sequential digits within the entire range. The complexity analysis highlights the efficiency of this approach, with both time and space complexity being constant, making it suitable for all input sizes within the problem's constraints.
