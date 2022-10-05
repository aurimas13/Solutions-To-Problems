class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(eval(f"{num1} + {num2}"))

# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.addStrings(num1 = "456", num2 = "77")  # num1 = "456", num2 = "77" -> "533"
    print(Solve)