# Solution of the problem
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


# Instantiating a class to return a value in PyCharm through command line
if __name__ == '__main__':
    Instant = Solution()
    # Solve = Instant.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)  # empty output - None
    Solve = Instant.isPalindrome(121)  # 1234 gives False, 121 - True
    print(Solve)
