from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(maxsize=None)
        def edit(x, y, i, j):
            # x: source, y: target
            # i, j -> unexplored
            if i == len(x):
                return len(y) - j  # insert the rest chars of target into source
            if j == len(y):
                return len(x) - i  # delete the rest chars in source

            if x[i] == y[j]:
                return edit(x, y, i + 1, j + 1)

            n_op1 = 1 + edit(x, y, i, j + 1)  # insert y[j] to source
            n_op2 = 1 + edit(x, y, i + 1, j)  # delete x[i] from source
            n_op3 = 1 + edit(x, y, i + 1, j + 1)  # replace x[i] by y[j]

            return min(n_op1, n_op2, n_op3)

        return edit(word1, word2, 0, 0)

# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.minDistance(word1="intention", word2="execution") 
    # word1 = "intention", word2 = "execution" -> 5
    print(Solve)
