class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        result = ''
        for j in s.split():
            result = result + j[::-1] + ' '
        return result.rstrip()


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.reverseWords(s = "Let's take LeetCode contest")
    print(Solve)
    # s = "Let's take LeetCode contest" -> "s'teL ekat edoCteeL tsetnoc"
