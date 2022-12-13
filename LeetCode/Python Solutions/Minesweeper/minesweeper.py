from typing import List
from collections import deque

class Solution:
    @staticmethod
    def updateBoard(board: List[List[str]], click: List[int]) -> List[List[str]]:
        seen = set()

        def scanProx(r, c):
            q = deque()

            q.append((r, c))

            while q:

                for i in range(len(q)):
                    c, d = q.popleft()
                    board[c][d] = 'B'
                    for x, y in directions:
                        valr, valc = c + x, d + y

                        if valr >= 0 and valr < len(b) and valc >= 0 and valc < len(b[0]):
                            if (valr, valc) in seen:
                                continue

                            if board[valr][valc] == "E":
                                if b[valr][valc] == 0:
                                    seen.add((valr, valc))
                                    q.append((valr, valc))
                                else:
                                    board[valr][valc] = str(b[valr][valc])

        b = [[0 for i in range(len(board[0]))] for j in range(len(board))]

        directions = [[1, 1], [1, 0], [1, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [0, -1]]

        for r in range(len(b)):
            for c in range(len(b[0])):

                if board[r][c] == 'M':

                    for x, y in directions:

                        valr, valc = r + x, c + y

                        if valr >= 0 and valr < len(b) and valc >= 0 and valc < len(b[0]):
                            if board[valr][valc] == "E":
                                b[valr][valc] += 1

        x, y = click[0], click[1]

        if board[x][y] == 'E':
            if b[x][y] == 0:
                board[x][y] = 'B'
                scanProx(x, y)
            else:
                board[x][y] = str(b[x][y])
        elif board[x][y] == 'M':
            board[x][y] = 'X'

        return board


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0])
    # board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
    # -> [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    print(Solve)