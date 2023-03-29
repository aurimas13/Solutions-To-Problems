from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # Define modulo constant
        MOD = 1000000007
        
        # Get pizza dimensions
        rows, cols = len(pizza), len(pizza[0])

        # Precompute prefix sum of apples in the pizza
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                prefix_sum[r + 1][c + 1] = prefix_sum[r + 1][c] + prefix_sum[r][c + 1] - prefix_sum[r][c] + (pizza[r][c] == 'A')

        # Helper function to check if there is at least one apple in a slice
        def has_apple(r1, c1, r2, c2):
            return prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r2 + 1][c1] - prefix_sum[r1][c2 + 1] + prefix_sum[r1][c1] > 0

        # Initialize memoization table
        memo = {}

        # Define recursive function for dynamic programming
        def dp(r, c, k):
            if (r, c, k) in memo:
                return memo[(r, c, k)]


            # If only one piece is left, check if it has at least one apple
            if k == 1:
                return int(has_apple(r, c, rows - 1, cols - 1))

            ways = 0

            # Cut vertically
            for nr in range(r + 1, rows):
                if has_apple(r, c, nr - 1, cols - 1):
                    ways = (ways + dp(nr, c, k - 1)) % MOD

            # Cut horizontally
            for nc in range(c + 1, cols):
                if has_apple(r, c, rows - 1, nc - 1):
                    ways = (ways + dp(r, nc, k - 1)) % MOD

            memo[(r, c, k)] = ways
            return ways

        # Call the recursive function to compute the result
        return dp(0, 0, k)


# Checking in terminal
if name == "main":
    s = Solution()
    pizza = ["A..", "AAA", "..."]
    k = 3
    print(s.ways(pizza, k)) # Output: 3
