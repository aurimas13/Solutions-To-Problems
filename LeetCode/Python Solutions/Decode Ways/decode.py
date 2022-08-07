class Solution:
    def numDecodings(self, s: str) -> int:

        memo = dict()

        def getDecodings(index, s):

            if index in memo:
                return memo[index]

            # If got to the end of the string return 1
            if index == len(s):
                return 1

            # If 0, cannot decode (1 - 26 only A-Z)
            if s[index] == "0":
                return 0

            if index == len(s) - 1:
                return 1

            answer = getDecodings(index + 1, s)

            # Double digit
            if int(s[index: index + 2]) <= 26:
                answer += getDecodings(index + 2, s)

            memo[index] = answer
            return answer

        return getDecodings(0, s)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.numDecodings("12")  # "12" -> 2 | "226" -> 3 | "06" -> 0
    print(Solve)

# OR

# def numDecodings(self, s: str) -> int:
#         def dfs(i):
#             if i >= len(s):
#                 return 1
#             if s[i] == "0":
#                 return 0
#             if i in dp:
#                 return dp[i]
#             res = 0
#             for j in range(i+1,len(s)+1):
#                 if 0 < int(s[i:j]) <= 26:
#                     res += dfs(j)
#             dp[i] = res
#             return dp[i]
#         dp = {}
#         return dfs(0)\
