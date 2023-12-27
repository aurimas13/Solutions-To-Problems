The problem description of "Maximal Network Rank" is found [here](https://leetcode.com/problems/maximal-network-rank/description/) while the slution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Maximal%20Network%20Rank/maximal.java).

To check the solution in terminal first compile Java file as `javac maximum.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

**Complexities**:

- *Time Complexity*: `O(n^2)` because of the nested loops to check the combination of cities.
- *Space Complexity*: `O(n + m)` or simply `O(n)` where n is the number of cities and m is the number of roads. The count array takes O(n) space and the connected set can have at most 2m elements (because each road results in two entries).