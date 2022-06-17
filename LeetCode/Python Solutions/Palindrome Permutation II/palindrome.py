from typing import List
from collections import Counter
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        nn, result = len(s), []

        def getPerm(comb, counter):
            if len(comb) == nn:
                result.append(comb)
                return

            for letter in counter:
                if counter[letter] > 0:
                    new_counter = counter.copy()
                    new_counter[letter] -= 2
                    getPerm(letter + comb + letter, new_counter)

        counter = Counter(s)

        odds = []
        for num in counter.keys():
            if counter[num] % 2 != 0:
                odds.append(num)
                counter[num] -= 1

        if len(odds) > 1:
            return []

        start = odds[0] if len(odds) == 1 else ""
        getPerm(start, counter)

        return result


# Checking in console
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.generatePalindromes("aabb")  #  "aabb" -> ['baab', 'abba']
    print(Solve)
