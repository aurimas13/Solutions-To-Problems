class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = tuple(reversed(text1))
        text2 = tuple(reversed(text2))

        m = len(text1)
        n = len(text2)

        memo = [0] * (n + 1)
        for i in range(1, m + 1):
            diag = 0
            for j in range(1, n + 1):
                tmp = memo[j]
                memo[j] = diag + 1 if text1[i - 1] == text2[j - 1] else max(memo[j], memo[j - 1])
                diag = tmp

        return memo[n]

# Tests
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestCommonSubsequence(text1 = "abc", text2 = "abc" ) 
    # text1 = "abc", text2 = "abc" -> 3
    print(Solve)
    Solve = Sol.longestCommonSubsequence(text1 = "abc", text2 = "def" )  
    # text1 = "abc", text2 = "def" -> 0
    print(Solve)


