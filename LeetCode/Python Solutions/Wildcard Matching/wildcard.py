class Solution:

    def removeDummyStars(self, p):
        if p == '':
            return p
        p1 = [p[0], ]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

    def isMatch(self, s: str, p: str) -> bool:
        p = self.removeDummyStars(p)
        dp = [(len(p) + 1) * [False] for _ in range(len(s) + 1)]
        dp[0][0] = True
        if len(p) > 0 and p[0] == '*':
            dp[0][1] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[len(s)][len(p)]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isMatch(s = "cb", p = "?a")  # s = "cb", p = "?a" -> false | s = "aa", p = "*" -> true
    print(Solve)
