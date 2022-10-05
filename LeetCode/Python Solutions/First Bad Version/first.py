class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left < right:
            v = (left + right) // 2

            if isBadVersion(v):
                right = v
            else:
                left = v + 1

        if isBadVersion(right):
            return right

        return -1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.firstBadVersion(n = 5)  # n = 5, bad = 4 -> 4
    print(Solve)
