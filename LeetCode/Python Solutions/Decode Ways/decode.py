class Solution:
    def numDecodings(self, s: str) -> int:
        
        # base cases:
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        # initialize the dp array
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        
        # fill in the rest of the dp array
        for i in range(2, len(s) + 1):
            # check if we can decode the current digit alone
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            # check if we can decode the current and previous digits as a double-digit number
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]
        
        return dp[-1]


# Tests:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.numDecodings("12")  
    # "12" -> 2 | "226" -> 3 | "06" -> 0
    print(Solve)
