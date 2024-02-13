Problem description of "Find First Palindromic String in the Array" can be found [here](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/) while the solution is found [here](https://github.com/aurimas13/LeetCode-HR-MAANG/blob/main/LeetCode/Java%20Solutions/Find%20First%20Palindromic%20String%20in%20the%20Array/first.java).

To check the solution in terminal first compile Java file as `javac find.java`, then run the command as follows `java Solution` and it will check tests and if the solution works correctly.

## Implementation

It efficiently solves the problem by iterating through each word in the given list or array and checking if it is a palindrome. The  Java solution manually compares characters from both ends towards the center to determine if a word is a palindrome. If a palindrome is found, it is immediately returned as the result; otherwise, after checking all words, an empty string is returned to indicate that no palindromic string was found in the input. This approach ensures that the solution is straightforward and efficient, with a clear step-by-step process for identifying the first palindromic word.