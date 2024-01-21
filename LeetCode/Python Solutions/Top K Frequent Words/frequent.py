from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count the frequency of each word
        word_counts = Counter(words)

        # Sort words by frequency and lexicographical order
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

        # Return the top k frequent words
        return [word for word, count in sorted_words[:k]]


# Test the function in the local environment
if __name__ == "__main__":
    s = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(s.topKFrequent(words, k))  # Output: ["i", "love"]

