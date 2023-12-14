class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Initialize the dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill in the dp array
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Calculate the minimum number of deletions required
        lcs_length = dp[m][n]
        return m + n - 2 * lcs_length

# Tests
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.minDistance(word1 = "sea", word2 = "eat")  
    # "sea", "eat" -> 2
    print(Solve)