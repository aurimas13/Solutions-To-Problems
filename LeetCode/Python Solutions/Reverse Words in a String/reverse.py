class Solution:
    @staticmethod
    def reverseWords(s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.reverseWords(s = "the sky is blue")
    print(Solve)
    # s = "the sky is blue" -> "blue is sky the"
    # s = "a good   example" -> "example good a"
