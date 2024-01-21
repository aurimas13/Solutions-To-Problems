class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Initialize the dynamic programming table
        dp = [0.0] * (n + maxPts + 1)

        # Set the base case values
        for i in range(k, n + 1):
            dp[i] = 1.0

        # Calculate the probability of reaching each score
        S = min(n - k + 1, maxPts)
        for i in range(k - 1, -1, -1):
            dp[i] = S / maxPts
            S += dp[i] - dp[i + maxPts]

        # Return the probability of reaching score 0
        return dp[0]

# Complexity Analysis:
# The time complexity of this solution is O(n + maxPts) where n is the input value and maxPts is the maximum points allowed.
# The space complexity is O(n + maxPts) as we use a dynamic programming table to store the probabilities.

# Tests
if __name__ == "__main__":
    solution = Solution()
    print(solution.new21Game(10, 1, 10))  # 1.0
    print(solution.new21Game(6, 1, 10))  # 0.6
    print(solution.new21Game(21, 17, 10))  # 0.7327777870686075
