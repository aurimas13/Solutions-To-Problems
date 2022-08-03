from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict: return False
        intervals = []

        for w in wordDict:
            startIndex = 0
            while True:
                try:
                    index = s.index(w, startIndex)
                except ValueError:
                    break
                intervals.append([index, index + len(w) - 1])
                startIndex = index + 1

        intervals.sort()

        searching = {0}
        for interval in intervals:
            start, end = interval
            if start in searching:
                if end == len(s) - 1:
                    return True
                else:
                    searching.add(end + 1)

        return False

if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.wordBreak("applepenapple", ["apple","pen"])  # s = "applepenapple", wordDict = ["apple","pen"]-> True | s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] -> False
    print(Solve)
