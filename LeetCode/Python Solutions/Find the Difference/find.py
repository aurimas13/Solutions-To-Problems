class Solution:
    @staticmethod
    def findTheDifference(s: str, t: str) -> str:
        r = 0
        for i in t:
            r = r + ord(i)
        for i in s:
            r = r - ord(i)
        return chr(r)


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.findTheDifference(s = "abcd", t = "abcde")
    # s = "", t = "y" -> "y"
    # s = "abcd", t = "abcde" -> "e"
    print(Solve)
