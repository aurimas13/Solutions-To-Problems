from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(list(s)) == Counter(list(t))

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isAnagram(s = "anagram", t = "nagaram") # s = "anagram", t = "nagaram" -> True | s = "rat", t = "car" -> False
    print(Solve)
