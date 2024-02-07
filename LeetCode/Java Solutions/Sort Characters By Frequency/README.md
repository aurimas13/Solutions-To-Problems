Problem description of "Sort Characters By Frequency" can be found [here](https://leetcode.com/problems/sort-characters-by-frequency/) and its solution [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Java%20Solutions/Sort%20Characters%20By%20Frequency/sort.java).

To check the solution in terminal first compile Java file as `javac sort.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implemetatiom

The Java solution manually counts the frequencies using a `HashMap`, then uses a `PriorityQueue` (max heap) to sort characters by frequency. It builds the result string by repeatedly removing the characters from the priority queue and appending them to a `StringBuilder` according to their frequency. This method effectively utilizes Java's collection framework to implement the frequency sorting logic