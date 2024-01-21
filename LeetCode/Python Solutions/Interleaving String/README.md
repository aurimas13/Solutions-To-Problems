The problem description is found [here](https://leetcode.com/problems/interleaving-string/description/) while the solution is found [here](https://github.com/aurimas13/Solutions-To-Problems/blob/main/LeetCode/Python%20Solutions/Interleaving%20String/interleaving.py).

**Explanation**:

1. If the sum of lengths of s1 and s2 is not equal to the length of s3, return False.
2. Initialize a 2D array dp with dimensions (len(s1)+1) x (len(s2)+1). The value dp[i][j] is True if the substring s3[:i+j] can be formed by interleaving s1[:i] and s2[:j].
3. Iterate over the lengths of s1 and s2 and fill the dp table.
4. Return dp[len(s1)][len(s2)] which represents if s3 can be formed by interleaving s1 and s2.

**Implementation**:

Imagine an online platform where you can create a custom playlist by merging two existing playlists, but the order of songs in each playlist should remain the same in the custom playlist. Given two playlists (s1 and s2) and a custom playlist (s3), this algorithm can help in verifying whether the custom playlist is a valid merge of the two original playlists or not.



