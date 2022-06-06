class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)  # empty output - None
    print(Solve)