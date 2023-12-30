class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter

        # Count all characters in all words
        total_count = Counter(''.join(words))

        # Check if each character's total count is divisible by the number of words
        for char, count in total_count.items():
            if count % len(words) != 0:
                return False

        return True
