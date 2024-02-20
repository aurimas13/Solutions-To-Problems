The problem description of "Power of Two" is found [here](https://leetcode.com/problems/power-of-two/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Power%20of%20Two/power.java).

To check the solution in terminal first compile Java file as `javac power.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

- The condition `n > 0` ensures that we are only considering positive integers since negative integers and zero cannot be powers of two according to the problem statement.

- The bitwise operation `n & (n - 1)` works by clearing the lowest set bit of `n`. For numbers that are powers of two, there is exactly one set bit in their binary representation. Subtracting 1 from such a number flips all the bits to the right of the set bit (including the set bit itself), resulting in a number where all bits to the right of the original set bit are now set, and the original set bit is cleared. The bitwise AND of this number with the original number will be 0 since they have no set bits in common.

- For numbers that are not powers of two (and have more than one set bit), this operation will not result in 0 because there will still be other set bits remaining.
