class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        for i in range(len(s), -1,-1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                surfix = s[i:]
                return "".join(surfix[::-1])+s


# Checking in console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.shortestPalindrome(s="abcd")  # s = "abcd" -> "dcbabcd"
    print(Solve)
