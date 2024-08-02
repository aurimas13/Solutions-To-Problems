from typing import List


class Solution:
    @staticmethod
    def minHeightShelves(books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            width, height = books[i - 1]
            dp[i] = dp[i - 1] + height
            j = i - 1
            while j > 0 and width + books[j - 1][0] <= shelfWidth:
                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1
        return dp[n]


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6)
    # books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4 -> 6
    # books = [[1,3],[2,4],[3,2]], shelfWidth = 6 -> 4
    print(Solve)
