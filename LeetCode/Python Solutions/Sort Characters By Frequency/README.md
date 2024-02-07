Problem description of "Sort Characters By Frequency" can be found [here](https://leetcode.com/problems/sort-characters-by-frequency/) and its solution [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Python%20Solutions/Sort%20Characters%20By%20Frequency/sort.py).

## Implemetatiom

The Python solution uses the `Counter` class to count the frequencies of each character in the string. It then sorts the characters by frequency (and lexicographically as a tie-breaker) and constructs the result string by concatenating multiples of each character according to its frequency. This approach is concise and leverages Python's standard library for efficient counting and sorting.