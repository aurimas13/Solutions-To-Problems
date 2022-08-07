class Solution:
    def numDecodings(self, s: str) -> int:
            def dfs(i):
                if i >= len(s):
                    return 1
                if s[i] == "0":
                    return 0
                if i in dp:
                    return dp[i]
                res = 0
                for j in range(i+1,len(s)+1):
                    if 0 < int(s[i:j]) <= 26:
                        res += dfs(j)
                dp[i] = res
                return dp[i]
            dp = {}
            return dfs(0)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.numDecodings("12")  #  "12" -> 2 | "226" -> 3 | "06" -> 0
    print(Solve)

