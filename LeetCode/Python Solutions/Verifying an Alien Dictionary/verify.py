from typing import List


class Solution:
    @staticmethod
    def isAlienSorted(words: List[str], order: str) -> bool:
        dct = {}
        k = ord('a')
        for i in order:
            dct[i] = chr(k)
            k += 1
        prev = ""
        for w in words:
            cur = ""
            for c in w:
                cur += dct[c]
            if cur < prev:
                return False
            prev = cur
        return True


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz")
    # words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz" -> true
    # words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz" -> false
    print(Solve)
