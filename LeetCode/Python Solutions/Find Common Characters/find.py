from typing import List
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Initialize with the first word's character count
        common_count = Counter(words[0])

        # Intersect the counts with the remaining words
        for word in words[1:]:
            word_count = Counter(word)
            for char in common_count.keys():
                if char in word_count:
                    common_count[char] = min(common_count[char], word_count[char])
                else:
                    common_count[char] = 0

        # Build the result list based on the final common counts
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result

# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.commonChars(["bella", "label", "roller"]))  # Output: ["e","l","l"]
    print(sol.commonChars(["cool", "lock", "cook"]))  # Output: ["c","o"]
