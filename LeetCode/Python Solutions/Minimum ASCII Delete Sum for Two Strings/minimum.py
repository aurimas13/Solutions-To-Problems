class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # length of the strings
        len1, len2 = len(s1), len(s2)
        
        # create a 2D DP table, the size is (len1+1) * (len2+1)
        # dp[i][j] represents the minimum ASCII delete sum for s1[0..i) and s2[0..j)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        
        # Initialize the first column
        for i in range(1, len1+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        # Initialize the first row
        for j in range(1, len2+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])
        
        # Fill the DP table using the recursion formula
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                # If current characters of both strings are same, no need to delete
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # Otherwise, delete either the current character of s1 or s2,
                # choose the one which costs less
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        
        # Return the final result
        return dp[len1][len2]

