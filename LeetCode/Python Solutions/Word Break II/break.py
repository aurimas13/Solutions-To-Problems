from typing import List


class Solution:
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for i in range(len(s) + 1)]
        dp[0].append([])
        for i in range(len(dp)):
            if dp[i]:
                for word in wordDict:
                    offset = len(word)
                    if s[i:].startswith(word):
                        for sentence in dp[i]:
                            dp[i + offset].append(sentence + [word])
        result = []
        for sent in dp[-1]:
            result.append(" ".join(sent))
        return result


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"])  # s
    # = "catsandog", wordDict = ["cats","dog","sand","and","cat"] -> [] |  s = "pineapplepenapple", wordDict = [
    # "apple","pen","applepen","pine","pineapple"] -> ["pine apple pen apple","pineapple pen apple","pine applepen
    # apple"]
    print(Solve)
