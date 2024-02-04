The problem description of "Minimum Window Substring" is found [here](https://leetcode.com/problems/minimum-window-substring/) and the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Minimum%20Window%20Substring/minimum.java).

To check the solution in terminal first compile Java file as `javac minimum.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The solution employs a sliding window approach to efficiently find the minimum window substring that contains all characters of t in s. The algorithm expands the window by moving the right pointer and contracts the window by moving the left pointer while maintaining a count of the required characters using hash maps. This ensures that we only consider valid substrings and efficiently find the minimum length window that satisfies the condition. The use of two pointers with hash maps allows for maintaining the current window's character counts, enabling the algorithm to check if the window contains all characters of t and adjust the window size accordingly.
