class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c for c in s.lower() if c.isalnum()]
        print(new_s)
        return new_s == new_s[::-1]


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isPalindrome(s = "A man, a plan, a canal: Panama") # s = "A man, a plan, a canal: Panama" -> true | "race a car" -> false
    print(Solve)
