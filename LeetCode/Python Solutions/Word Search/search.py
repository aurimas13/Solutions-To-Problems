from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0 or len(word) == 0 or len(word) > len(board) * len(board[0]):
            return False

        visited = [[False] * len(board[0]) for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, visited, ''):
                    return True
        return False

    def dfs(self, board, row, col, word, visited, path):
        if visited[row][col]:
            return False
        if board[row][col] != word[len(path)]:
            return False
        path = path + board[row][col]
        if path == word:
            return True

        visited[row][col] = True
        if col - 1 >= 0 and self.dfs(board, row, col - 1, word, visited, path):
            return True
        if row - 1 >= 0 and self.dfs(board, row - 1, col, word, visited, path):
            return True
        if col + 1 < len(board[0]) and self.dfs(board, row, col + 1, word, visited, path):
            return True
        if row + 1 < len(board) and self.dfs(board, row + 1, col, word, visited, path):
            return True

        visited[row][col] = False


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") 
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" -> true
    # board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE" -> true
    print(Solve)