class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        # dp[i] represents the minimum height for books[i:]
        dp = [float('inf')] * (n + 1)
        dp[n] = 0  # Base case: no books means 0 height

        for i in range(n - 1, -1, -1):
            width = 0
            height = 0
            j = i
            while j < n and width + books[j][0] <= shelfWidth:
                width += books[j][0]
                height = max(height, books[j][1])
                dp[i] = min(dp[i], height + dp[j + 1])
                j += 1

        return dp[0]