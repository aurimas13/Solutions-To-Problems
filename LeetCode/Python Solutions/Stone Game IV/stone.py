class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # Initialize a list to store the winning status for each number
        dp = [False] * (n + 1)

        # Iterate through the numbers from 1 to n
        for i in range(1, n + 1):
            # Check if there is a square number that results in a losing state for the opponent
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i ** 0.5) + 1))

        return dp[n]

# Test cases to try in the terminal/console
# Checking in PyCharm console:
if __name__ == '__main__':
    solution = Solution()
    print(solution.winnerSquareGame(1))  # Output: True
    print(solution.winnerSquareGame(2))  # Output: False
    print(solution.winnerSquareGame(4))  # Output: True
    print(solution.winnerSquareGame(7))  # Output: False
    print(solution.winnerSquareGame(17))  # Output: False
