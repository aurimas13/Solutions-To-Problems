Problem description og "Set Mismatch" can be found [here](https://leetcode.com/problems/set-mismatch/) while its solution can be found [here](https://github.com/aurimas13/LeetCode-HackerRank-MAANG/blob/main/LeetCode/Java%20Solutions/Set%20Mismatch/set.java).
    
To check the solution in terminal first compile Java file as `javac set.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The provided Java solution effectively find the duplicated and missing numbers in the array. The approach involves iterating through the array while keeping track of seen numbers using a set in Python or a boolean array in Java. When a repeated number is detected, it's marked as the duplicated number. Subsequently, by iterating through the range from 1 to n, we find the missing number that is not present in the set or boolean array. This method ensures accurate identification of both the duplicated and missing numbers with linear time complexity, making it efficient and suitable for large datasets within the given constraints.