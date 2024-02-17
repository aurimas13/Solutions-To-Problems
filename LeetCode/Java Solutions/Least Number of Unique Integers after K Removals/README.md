The problem description of "Least Number of Unique Integers after K Removals" can be found [here](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/) and the solution can be found [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Java%20Solutions/Least%20Number%20of%20Unique%20Integers%20after%20K%20Removals/least.java).

To check the solution in terminal first compile Java file as `javac least.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Explanation

`Greedy Choice`: The strategy of using bricks for smaller jumps and ladders for larger jumps ensures we can cover the maximum distance possible because ladders can overcome any height difference without being "consumed" like bricks.

`Priority Queue/Min-Heap`: It keeps track of the height differences where ladders have been "provisionally" used. By keeping this in a min-heap, we ensure that when we need to switch from using a ladder to using bricks, we use bricks on the smallest height difference possible.

`Iterating through Buildings`: For each pair of consecutive buildings, if the next building is higher, we account for the height difference either by planning to use a ladder (adding the difference to the heap) or, if we exceed the number of ladders, by using bricks for the smallest differences first (removing from the heap).

`Returning the Index`: If at any point bricks become negative, it means we cannot make the jump to the next building, and we return the current index. If we finish iterating through the buildings without running out of bricks, it means we can reach the last building.

## Explanation

- The core logic involves counting frequencies, sorting or prioritizing them based on frequency, and then iteratively removing elements based on their frequency until k is exhausted.

- The correct output for the example [5,5,4] with k = 1 should indeed be 2, as removing one occurrence of 4 leaves two unique integers, 5 and 4. The original output seems to be consistent with understanding the problem statement; thus, any confusion might stem from misinterpreting the result or an error in submitting the problem solution.