from typing import List


class Solution:
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        # Rows, Cols and Quadrant will store seen numbers at the Nth bit
        rows = [0] * 9
        cols = [0] * 9
        quadrant = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                # character to number
                num = ord(board[i][j]) - ord('0')

                # Shift 1 to num position
                bit = (1 << num)

                # if number has been seen at a row, column or quadrant, AND operation will
                # result in a greater than zero number (which is bit), if haven't seen,
                # AND operation will result to zero.
                if (bit & rows[i]) or (bit & cols[j]) or (bit & quadrant[i // 3][j // 3]):
                    return False

                # Marking rows, cols and quadrant that num has been seen at that position.
                rows[i] ^= bit
                cols[j] ^= bit
                quadrant[i // 3][j // 3] ^= bit

        return True


# Test Cases:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isValidSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) # board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]] -> true
    print(Solve)
