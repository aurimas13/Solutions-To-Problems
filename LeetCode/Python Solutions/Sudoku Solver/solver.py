from typing import List


class Solution:
    @staticmethod
    def solveSudoku(board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cuadrant = []
        for _ in range(3):
            cuadrant.append([set() for _ in range(9)])

        # Stack or positions to be filled
        s = []
        # Useful to iterate numbers as strings
        numStr = [str(num) for num in range(1, 10)]

        # Fill
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    cols[j].add(board[i][j])
                    rows[i].add(board[i][j])
                    cuadrant[i // 3][j // 3].add(board[i][j])
                else:
                    s.append((i, j))

        def backtrack():
            # No elements missing
            if len(s) == 0:
                return True

            i, j = s.pop()
            for num in numStr:
                if num not in cols[j] and num not in rows[i] and num not in cuadrant[i // 3][j // 3]:
                    board[i][j] = num
                    cols[j].add(num)
                    rows[i].add(num)
                    cuadrant[i // 3][j // 3].add(num)

                    if backtrack():
                        return True

                    cuadrant[i // 3][j // 3].remove(num)
                    rows[i].remove(num)
                    cols[j].remove(num)
                    board[i][j] = "."

            # Return the position to the stack to re-process later
            s.append((i, j))
            return False

        backtrack()
