class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isPalindrome(121)  # 1234 gives False, 121 - True
    print(Solve)

