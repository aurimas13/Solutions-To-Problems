class Solution:
    def countSubstrings(self, s: str) -> int:

        if not s: return None
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = 0

        for i in reversed(range(n)):  # bc dp[i][j] depends on dp[i+1][j], so check larger i first
            for j in range(i, n):
                if j - i < 2 and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1
                elif dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    ans += 1

        return ans


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.countSubstrings(s = "aaa")  # s = "abc" -> 3 | s = "aaa" -> 6
    print(Solve)