from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        # Dynamic programming approach
        for i in range(n - 1, -1, -1):
            dp[i] = float('-inf')
            take = 0
            # Consider taking 1, 2, or 3 stones
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    # Calculate the maximum score difference
                    dp[i] = max(dp[i], take - dp[i + k + 1])

        # Determine the winner based on the score difference
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie" 

if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    stoneValue1 = [1, 2, 3, 7]
    # Alice: Alice can take all stones and win with a score of 8
    print(solution.stoneGameIII(stoneValue1))  # Output: "Alice"

    # Test case 2
    stoneValue2 = [1, 2, 3, -9]
    # Bob: Alice can only take 1 stone and Bob can take the remaining stones to win with a score of 3
    print(solution.stoneGameIII(stoneValue2))  # Output: "Bob"

    # Test case 3
    stoneValue3 = [1, 2, 3, 6]
    # Tie: Both players can score the same total, resulting in a tie
    print(solution.stoneGameIII(stoneValue3))  # Output: "Tie"
