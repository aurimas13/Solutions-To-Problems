Problem description of "Group Anagrams" can be found [here](https://leetcode.com/problems/group-anagrams/) while the solution is found [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Python%20Solutions/Group%20Anagrams/group.py).

## Implementation

The Python solution leverages a defaultdict for grouping anagrams, which simplifies the logic for handling new groups. By sorting the characters of each word, we use the sorted word as a key to group all anagrams together. This approach ensures that all anagrams are grouped efficiently with a single traversal of the input list, making the solution highly efficient for large datasets.