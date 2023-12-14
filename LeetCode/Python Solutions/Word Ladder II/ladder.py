from typing import List
from collections import defaultdict


class Solution:
    @staticmethod
    def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        queue = [beginWord]
        prevDict = defaultdict(list)

        while queue:
            toDelete = set()

            for word in queue:
                for i in range(len(word)):
                    for alpha in "abcdefghijklmnopqrstuvwxyz":
                        nextWord = word[:i] + alpha + word[i + 1:]
                        if nextWord in wordSet:
                            toDelete.add(nextWord)
                            prevDict[nextWord].append(word)

            queue = list(toDelete)
            wordSet -= toDelete

            if endWord in toDelete:
                break

        ans = []
        dfsBacktrack(prevDict, beginWord, endWord, [], ans)

        return ans


def dfsBacktrack(prevDict, beginWord, currWord, currSequence, ans):
    if beginWord == currWord:
        ans.append([beginWord] + currSequence[::-1])
        return

    for prevWord in prevDict[currWord]:
        dfsBacktrack(prevDict, beginWord, prevWord, currSequence + [currWord], ans)


if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.findLadders( beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"])
    #  beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] ->
    #  [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    # beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"] -> []
    print(Solve)
