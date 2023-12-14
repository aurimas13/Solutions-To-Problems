class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        return ' '.join(word[::-1] for word in words)


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.reverseWords(s = "Let's take LeetCode contest")
    print(Solve)
    # s = "Let's take LeetCode contest" -> "s'teL ekat edoCteeL tsetnoc"

