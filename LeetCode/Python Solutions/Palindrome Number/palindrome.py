# Solution of the problem
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


# Instantiating a class to return a value in a command line
if __name__ == '__main__':
    Solve = Solution.isPalindrome(1, 121)  # 1234 gives False
    print(Solve)
