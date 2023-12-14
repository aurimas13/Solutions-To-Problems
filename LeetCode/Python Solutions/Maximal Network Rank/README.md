The problem description of "Maximal Network Rank" is found [here](https://leetcode.com/problems/maximal-network-rank/description/) while the slution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Python%20Solutions/Maximal%20Network%20Rank/maximal.py).

**Complexities**:

- *Time Complexity*: `O(n^2)` because of the nested loops to check the combination of cities.
- *Space Complexity*: `O(n + m)` or simply `O(n)` where n is the number of cities and m is the number of roads. The count array takes O(n) space and the connected set can have at most 2m elements (because each road results in two entries).