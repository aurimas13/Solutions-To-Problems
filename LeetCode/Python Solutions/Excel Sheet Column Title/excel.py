class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))



# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.convertToTitle(columnNumber=701)
    # columnNumber = 701 -> "ZY"
    # columnNumber = 28 -> "AB"
    print(Solve)
