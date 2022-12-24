class Solution:
    @staticmethod
    def convertToTitle(columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.convertToTitle(columnNumber=701)
    # columnNumber = 701 -> "ZY"
    # columnNumber = 28 -> "AB"
    print(Solve)
