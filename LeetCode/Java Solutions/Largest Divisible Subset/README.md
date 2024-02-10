Problem description of 'Largest Divisible Subset' can be found [here](https://leetcode.com/problems/largest-divisible-subset/) and its solution [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Java%20Solutions/Largest%20Divisible%20Subset/largest.java).

To check the solution in terminal first compile Java file as `javac largest.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

The solution utilizes a center expansion technique to find all palindromic substrings in the given string `s`. By considering each character and each pair of consecutive characters as potential centers of palindromes, we ensure that all palindromic substrings are counted, including those of odd and even lengths. The key part of the solution involves expanding around these centers and counting palindromes until the substring no longer forms a palindrome. This method is both efficient and straightforward, allowing us to count all palindromic substrings with a simple and elegant algorithm.