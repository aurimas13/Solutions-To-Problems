Problem description of "Group Anagrams" can be found [here](https://leetcode.com/problems/group-anagrams/) while the solution is found [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Java%20Solutions/Group%20Anagrams/group.java).

To check the solution in terminal first compile Java file as `javac group.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The Java solution uses a HashMap to achieve the same effect as the Python version. It sorts the characters of each word to use as keys for grouping anagrams. Utilizing Java's standard library functions for sorting (`Arrays.sort`) and managing collections (`ArrayList` and `HashMap`), the solution is both concise and efficient, allowing for fast grouping of anagrams with minimal overhead.