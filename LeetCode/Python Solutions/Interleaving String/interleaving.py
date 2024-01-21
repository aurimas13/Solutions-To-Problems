class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # If the sum of lengths of s1 and s2 is not equal to s3
        if len(s1) + len(s2) != len(s3):
            return False
        
        # Initialize dp table
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        # Base cases
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # Fill the dp table
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        
        return dp[len(s1)][len(s2)]
