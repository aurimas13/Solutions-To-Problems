The problem description of "Sum of Subarray Minimums" can be found [here](https://leetcode.com/problems/sum-of-subarray-minimums/) while the solution can be found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Sum%20of%20Subarray%20Minimums/sum.java).

To check the solution in terminal first compile Java file as `javac sum.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The Java solution efficiently calculates the sum of minimums of all subarrays in an array. The approach utilizes a stack to find the previous and next smaller elements for each array element. By calculating the number of subarrays for which each element is the minimum and summing these products, we obtain the desired result. This method is very efficient, with a linear time complexity and a linear space complexity, making it well-suited for large arrays and fitting within the problem's constraints.