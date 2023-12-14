class Solution:
    def getPower(self, x: int) -> int:
        steps = 0
        while x != 1:
            if x % 2 == 0:
                x = x // 2
            else:
                x = 3 * x + 1
            steps += 1
        return steps

    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = []
        for i in range(lo, hi + 1):
            powers.append((i, self.getPower(i)))
        powers.sort(key=lambda x: (x[1], x[0]))
        return powers[k-1][0]


# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.getKth(lo = 12, hi = 15, k = 2)  
    # lo = 12, hi = 15, k = 2 -> 13
    # lo = 7, hi = 11, k = 4 -> 7
    print(Solve)