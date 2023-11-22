class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 1000000007
        valid_rows = self.generate_valid_rows(m)
        adj_matrix = self.build_adjacency_matrix(valid_rows)
        dp = [1] * len(valid_rows)
        
        for _ in range(n - 1):
            dp_next = [0] * len(valid_rows)
            for i, row in enumerate(valid_rows):
                for j, adj_row in enumerate(valid_rows):
                    if adj_matrix[i][j]:
                        dp_next[j] += dp[i]
                        dp_next[j] %= MOD
            dp = dp_next
        
        return sum(dp) % MOD

    def generate_valid_rows(self, m: int) -> list:
        valid_rows = []
        for i in range(3 ** m):
            row = []
            for j in range(m):
                row.append((i // (3 ** j)) % 3)
            if all(row[k] != row[k + 1] for k in range(m - 1)):
                valid_rows.append(tuple(row))
        return valid_rows

    def build_adjacency_matrix(self, valid_rows: list) -> list:
        adj_matrix = [[False] * len(valid_rows) for _ in range(len(valid_rows))]
        for i, row1 in enumerate(valid_rows):
            for j, row2 in enumerate(valid_rows):
                if all(row1[k] != row2[k] for k in range(len(row1))):
                    adj_matrix[i][j] = True
        return adj_matrix


# Tests:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.colorTheGrid(m = 1, n = 1) # m = 1, n = 1 -> 3
    # m = 1, n = 2 -> 6
    # m = 5, n = 5 -> 5809861234
    print(Solve)
