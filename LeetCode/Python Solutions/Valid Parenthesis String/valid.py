class Solution:
    def checkValidString(self, s: str) -> bool:
        minBalance, maxBalance = 0, 0
        for char in s:
            if char == '(':
                minBalance += 1
                maxBalance += 1
            elif char == ')':
                minBalance = max(minBalance - 1, 0)
                maxBalance -= 1
                if maxBalance < 0:
                    return False
            else:  # char == '*'
                minBalance = max(minBalance - 1, 0)
                maxBalance += 1
        
        return minBalance == 0

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.checkValidString(s = "(*))")  # s = "(*))" -> True
    print(Solve)
