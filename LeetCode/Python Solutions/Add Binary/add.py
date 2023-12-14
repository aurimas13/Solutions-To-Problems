class Solution:
    @staticmethod
    def addBinary(a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y > 0:
            a, b = x | y, x & y
            x, y = a & ~b, b << 1

        return bin(x)[2:]


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.addBinary(a = "11", b = "1")
    # a = "1010", b = "1011" -> "10101"
    # a = "11", b = "1" -> "100"
    print(Solve)
