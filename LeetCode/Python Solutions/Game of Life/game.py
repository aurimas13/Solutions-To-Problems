from typing import List


class Solution:
    @staticmethod
    def gameOfLife(board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        i = 0
        row, col = len(board), len(board[0])
        _one = set()
        for r in range(row):
            for c in range(col):
                if board[r][c] == 1:
                    _one.add((r, c))

        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for r in range(row):
            for c in range(col):
                live_neigh = 0

                for m, n in neighbours:
                    x = r + m
                    y = c + n

                    if (x, y) in _one:
                        live_neigh += 1

                if (r, c) in _one and (2 > live_neigh or live_neigh > 3):
                    board[r][c] = 0
                elif (r, c) not in _one and live_neigh == 3:
                    board[r][c] = 1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Sol.gameOfLife(board=[[1, 1], [1, 0]])

