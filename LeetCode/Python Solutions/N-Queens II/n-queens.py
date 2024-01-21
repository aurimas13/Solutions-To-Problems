class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(queen, queens):
            return all(q != queen and abs(queen - q) != len(queens) - i for i, q in enumerate(queens))

        def n_queens_helper(queens):
            if len(queens) == n:
                return 1
            return sum(n_queens_helper(queens + [q]) for q in range(n) if is_safe(q, queens))

        return n_queens_helper([])


def run_tests():
    solution = Solution()
    assert solution.totalNQueens(4) == 2
    assert solution.totalNQueens(1) == 1
    assert solution.totalNQueens(8) == 92
    print("All tests passed!")


# Checking in terminal
if __name__ == '__main__':
    run_tests()
