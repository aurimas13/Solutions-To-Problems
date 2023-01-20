from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def bfs(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O":
                return
            board[i][j] = "T"
            bfs(board, i + 1, j)
            bfs(board, i - 1, j)
            bfs(board, i, j + 1)
            bfs(board, i, j - 1)

        if not board:
            return
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            if board[i][0] == "O":
                bfs(board, i, 0)
            if board[i][cols - 1] == "O":
                bfs(board, i, cols - 1)
        for j in range(cols):
            if board[0][j] == "O":
                bfs(board, 0, j)
            if board[rows - 1][j] == "O":
                bfs(board, rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
    # board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # -> [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    print(Solve)
