class Solution:
    def getSum(self, a: int, b: int) -> int:
        values = []
        values.append(a)
        values.append(b)
        return sum(values)


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.getSum(2, 3) # 2, 3 -> 5 | a = 1, b = 2 -> 3
    print(Solve)
