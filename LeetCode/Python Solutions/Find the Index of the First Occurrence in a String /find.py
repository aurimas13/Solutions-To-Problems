from typing import List


class Solution:
    @staticmethod
    def strStr(haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        for i in range(m - n + 1):
            if haystack[i:i + n] == needle:
                return i

        return -1


# Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.strStr([1, 3, 4, 2, 2])
    # haystack = "sadbutsad", needle = "sad" -> 0
    # haystack = "leetcode", needle = "leeto" -> -1
    print(Solve)
