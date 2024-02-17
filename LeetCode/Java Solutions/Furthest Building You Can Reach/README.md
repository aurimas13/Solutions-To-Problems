The problem description of "Furthest Building You Can Reach" can be found [here](https://leetcode.com/problems/furthest-building-you-can-reach/) and the solution can be found [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Java%20Solutions/Furthest%20Building%20You%20Can%20Reach/furthest.java).

To check the solution in terminal first compile Java file as `javac furthest.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Explanation

`Greedy Choice`: The strategy of using bricks for smaller jumps and ladders for larger jumps ensures we can cover the maximum distance possible because ladders can overcome any height difference without being "consumed" like bricks.

`Priority Queue/Min-Heap`: It keeps track of the height differences where ladders have been "provisionally" used. By keeping this in a min-heap, we ensure that when we need to switch from using a ladder to using bricks, we use bricks on the smallest height difference possible.

`Iterating through Buildings`: For each pair of consecutive buildings, if the next building is higher, we account for the height difference either by planning to use a ladder (adding the difference to the heap) or, if we exceed the number of ladders, by using bricks for the smallest differences first (removing from the heap).

`Returning the Index`: If at any point bricks become negative, it means we cannot make the jump to the next building, and we return the current index. If we finish iterating through the buildings without running out of bricks, it means we can reach the last building.