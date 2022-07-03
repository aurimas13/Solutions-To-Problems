from typing import List
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1_list = [x for x in range(len(wordsDict)) if wordsDict[x] == word1]
        w2_list = [x for x in range(len(wordsDict)) if wordsDict[x] == word2]
        minimum = float('inf')
        i, j = 0, 0
        while i < len(w1_list) and j < len(w2_list):
            diff = w1_list[i] - w2_list[j]
            minimum = min(minimum, abs(diff))
            if diff < 0:  # Means the value of the current position is lower than the l2's, move the l1's pointer
                i += 1
            elif diff > 0:  # Quite similar
                j += 1
            else:
                break
        return minimum



# Checking in PyCharm/terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "makes")  # wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice" -> 3 | ["a","b","c","d","d"], "a", "d" -> 3
    print(Solve)
