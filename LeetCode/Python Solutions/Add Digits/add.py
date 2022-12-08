class Solution:
    @staticmethod
    def addDigits(num: int) -> int:
        return (num-1)%9 +1 if num else 0


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.addDigits(num = 38)
    # num = 0 -> 0
    # num = 38 -> 2
    print(Solve)

