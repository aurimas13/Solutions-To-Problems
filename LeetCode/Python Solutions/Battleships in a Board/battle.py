from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Initialize the count of battleships
        battleships = 0

        # Iterate through the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Check if the current cell is part of a battleship
                if board[i][j] == "X":
                    # Check if the current cell is the head of the battleship
                    if i == 0 or board[i - 1][j] != "X":
                        if j == 0 or board[i][j - 1] != "X":
                            battleships += 1

        # Return the count of battleships
        return battleships

# Test cases
if __name__ == "__main__":
    solution = Solution()

    assert solution.countBattleships([
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"]
    ]) == 2

    assert solution.countBattleships([
        [".", ".", ".", "X"],
        [".", "X", ".", "X"],
        [".", ".", ".", "."]
    ]) == 2

    assert solution.countBattleships([
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]) == 0

    assert solution.countBattleships([
        ["X", ".", ".", "X"]
    ]) == 2

    assert solution.countBattleships([
        ["X"],
        ["."],
        ["."],
        ["."]
    ]) == 1
