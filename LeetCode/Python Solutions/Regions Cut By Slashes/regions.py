import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.compile('^'+p+'$').match(s):
            return True
        return False


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isMatch(s = "ab", p = ".*")  #  s = "ab", p = ".*" ->> True | s = "aa", p = "a" -> False
    print(Solve)