from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        Words = set()
        m = len(board)
        n = len(board[0])
        map = [[0] * n for i in range(m)]
        for i in words:
            Words.add(i)
        prefix = set()
        for it in words:
            for j in range(len(it) - 1):
                prefix.add(it[:j + 1])

        def dfs(row, col, strin):
            parent = strin
            strin += board[row][col]
            if strin in prefix or strin in Words:
                map[row][col] = 1
                if strin in Words:
                    Words.remove(strin)
                    output.append(strin)
                for i, j in adjacent(row, col):
                    dfs(i, j, strin)
                map[row][col] = 0
            return

        def adjacent(row, col):
            res = []
            if row - 1 >= 0 and map[row - 1][col] == 0:
                res.append([row - 1, col])
            if row + 1 < m and map[row + 1][col] == 0:
                res.append([row + 1, col])
            if col + 1 < n and map[row][col + 1] == 0:
                res.append([row, col + 1])
            if col - 1 >= 0 and map[row][col - 1] == 0:
                res.append([row, col - 1])
            return res

        output = []
        for i in range(m):
            for j in range(n):
                map[i][j] = 1
                dfs(i, j, '')
                map[i][j] = 0
        return output


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findWords(board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]) # board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"] -> ["eat","oath"]
    print(Solve)
