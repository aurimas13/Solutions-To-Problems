from collections import defaultdict
from typing import List

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.endWord = False
        self.word = ''

    def insert(self, word):
        cur = self

        for c in word:
            cur = cur.children[c]

        cur.endWord = True
        cur.word = word

    def search(self, word):
        cur = self

        for c in word:
            if not cur.children[c].endWord:
                return False
            cur = cur.children[c]

        return True


class Solution:
    @staticmethod
    def longestWord(words: List[str]) -> str:
        trie = Trie()

        for word in words:
            trie.insert(word)

        ans = ''

        for word in words:
            if trie.search(word):
                if (len(word) > len(ans) or len(word) == len(ans) and word < ans):
                    ans = word

        return ans


    # Checking in terminal/console:
if __name__ == '__main__':
    Sol = Solution()
    Solve = Sol.longestWord(words = ["w","wo","wor","worl","world"])
    # words = ["w","wo","wor","worl","world"] -> "world"
    # words = ["a","banana","app","appl","ap","apply","apple"] -> "apple"
    print(Solve)
