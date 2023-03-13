class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        
        if n > 10:
            n = 10
            
        count = 10
        unique_digits = 9
        
        for i in range(2, n + 1):
            unique_digits *= (11 - i)
            count += unique_digits
            
        return count


# Checking in PyCharm:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.countNumbersWithUniqueDigits([5,2,6,1]) 
    # n = 2 -> 91
    # n = 0 -> 1
    print(Solve)
