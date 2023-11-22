from typing import List


class Solution(object):
    @staticmethod
    def solveNQueens(n):
        currRes = []
        res = []

        def backtrack(row, colSet, diagSet, antiDiagSet):
            # moved past the grid, we could place all
            if row == n:
                acc = []
                for r in currRes:
                    string = ['.'] * n
                    string[r] = 'Q'

                    acc.append(''.join(string))
                res.append(acc)

                return

            for col in range(n):
                diag = row - col
                antiDiag = row + col

                if (col in colSet) or (diag in diagSet) or (antiDiag in antiDiagSet):
                    continue

                currRes.append(col)
                colSet.add(col)
                diagSet.add(diag)
                antiDiagSet.add(antiDiag)

                backtrack(row + 1, colSet, diagSet, antiDiagSet)

                currRes.pop()
                colSet.remove(col)
                diagSet.remove(diag)
                antiDiagSet.remove(antiDiag)

        backtrack(0, set(), set(), set())

        return res


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.solveNQueens(n=4)  # n = 4 ->  [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print(Solve)
