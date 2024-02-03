Problem description of "Partition Array for Maximum Sum" can be found [here](https://leetcode.com/problems/partition-array-for-maximum-sum/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Partition%20Array%20for%20Maximum%20Sum/partition.java).

To check the solution in terminal first compile Java file as `javac partition.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The solution utilizes dynamic programming to solve the problem of maximizing the sum after partitioning the array with subarrays of length at most k. The approach involves iterating through the array and, for each position, considering all possible partitions up to k elements back. This allows calculating the maximum sum achievable by picking the maximum value within each partition and multiplying it by the partition's length. The dynamic programming array dp keeps track of the maximum sum achievable for every position in the array, ensuring an efficient solution with a time complexity of O(n * k), where n is the array's length. This method guarantees finding the optimal partitioning strategy to maximize the sum.
