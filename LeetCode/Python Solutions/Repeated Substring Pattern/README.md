The problem of "Repeated Substring Pattern" description is found [here](https://leetcode.com/problems/repeated-substring-pattern/description/) while the solution is [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Python%20Solutions/Repeated%20Substring%20Pattern/repeated.py).

**Explanation**:

1. **Understanding the Trick**:

If a string `s` is formed by repeating a substring, then you can visualize the pattern by thinking of the string as a loop.

For instance, with the string "ABAB", you can think of this as the pattern "AB" looping twice. If we take two copies of "ABAB" to form "ABABABAB", you can see there's overlap of the repeated pattern in the middle. Specifically, from the second character to the second last character, there's another "ABAB".

This is true for any repeating pattern. If the string is "ABCABC", then two copies give "ABCABCABCABC", and from the second character to the second last character there's another "ABCABC".

2. **Constructing the Trick**:

By creating the string `s + s` (i.e., two copies of `s` concatenated), and removing the first and the last character, we're essentially checking if the original string `s` exists in this overlapped region.