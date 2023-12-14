class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        # Moves map: each key can move to the following keys
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8],
                 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6],
                 8: [1, 3], 9: [2, 4]}

        # Initialize the count for each number for length 1
        count = [1] * 10

        # Dynamic Programming: iterate for length n
        for _ in range(n - 1):
            new_count = [0] * 10
            for num in range(10):
                for move in moves[num]:
                    new_count[move] = (new_count[move] + count[num]) % MOD
            count = new_count

        return sum(count) % MOD
