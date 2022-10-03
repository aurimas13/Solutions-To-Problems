from typing import List
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letters = [
            None,
            None,
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        ]
        iterables = list(letters[int(n)] for n in digits)
        return [''.join(x) for x in product(*iterables)]


# Checking in PyCharm/terminal
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.letterCombinations(digits="23")  # digits = "23" -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(Solve)
