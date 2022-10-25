# Solution of the problem
class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]
        # if str(x) == str(x)[::-1]:
        #     return True
        # else:
        #     return False


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isPalindrome(121)  # 1234 gives False, 121 - True
    print(Solve)
