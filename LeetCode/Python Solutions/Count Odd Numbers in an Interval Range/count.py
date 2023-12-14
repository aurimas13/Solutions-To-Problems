class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1 + low % 2 + high % 2) // 2


# Checking in Terminal/Console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countOdds(low = 3, high = 7)
    # low = 3, high = 7 -> 3
    # low = 8, high = 10 -> 1
    print(Solve)
    