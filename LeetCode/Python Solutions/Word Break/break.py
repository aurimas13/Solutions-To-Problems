from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # check if wordDict is empty
        if not wordDict:
            return False

        # create list of intervals where words in wordDict are found in s
        intervals = []
        for word in wordDict:
            start_index = 0
            while True:
                try:
                    index = s.index(word, start_index)
                except ValueError:
                    break
                intervals.append([index, index + len(word) - 1])
                start_index = index + 1

        # sort intervals by start index
        intervals.sort()

        # use set to keep track of possible start indices of remaining words
        possible_starts = {0}
        for interval in intervals:
            start, end = interval
            # check if current interval starts at a possible start index
            if start in possible_starts:
                # check if current interval ends at the end of s
                if end == len(s) - 1:
                    return True
                # add end index of current interval as a possible start index
                possible_starts.add(end + 1)

        return False


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.wordBreak("applepenapple", ["apple","pen"]) 
    # s = "applepenapple", wordDict = ["apple","pen"]-> True 
    # s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] -> False
    print(Solve)
