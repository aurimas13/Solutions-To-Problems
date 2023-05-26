from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if (i, m) in memo:
                return memo[(i, m)]

            if i + 2 * m >= n:
                return suffix_sum[i]

            max_stones = float('-inf')
            for x in range(1, 2 * m + 1):
                next_m = max(m, x)
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, next_m))

            memo[(i, m)] = max_stones
            return max_stones

        return dp(0, 1)


# Tests:
if __name__ == "__main__":
    solution = Solution()
    
    # Example test cases
    print(solution.stoneGameII([2, 7, 9, 4]))  # Output: 10
    print(solution.stoneGameII([1, 2, 3, 4, 5, 100]))  # Output: 104
