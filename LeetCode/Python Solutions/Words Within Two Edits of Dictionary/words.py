from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def isMatch(s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            if len(s1) != len(s2):
                return False
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                    if count > 1:
                        return False
            return True

        def isTwoEditMatch(s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            if len(s1) != len(s2):
                return False
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count == 2

        wordSet = set(dictionary)
        results = []
        for query in queries:
            if query in wordSet:
                results.append(query)
            else:
                for word in wordSet:
                    if isMatch(query, word) or isTwoEditMatch(query, word):
                        results.append(query)
                        break
        return results


# Running in terminal:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.twoEditWords(queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"])
     # queries = ["word","note","ants","wood"], dictionary = ["wood","joke","moat"]
     # -> ["word","note","wood"]
     # queries = ["yes"], dictionary = ["not"]
     # []
    print(Solve)
