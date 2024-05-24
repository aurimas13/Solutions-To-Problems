from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def get_word_score(word: str) -> int:
            return sum(score[ord(ch) - ord('a')] for ch in word)
        
        def can_form_word(word: str, letter_count: Counter) -> bool:
            word_count = Counter(word)
            for ch in word_count:
                if word_count[ch] > letter_count[ch]:
                    return False
            return True
        
        def backtrack(index: int, current_score: int, letter_count: Counter) -> int:
            if index == len(words):
                return current_score
            
            max_score = backtrack(index + 1, current_score, letter_count)
            
            word = words[index]
            if can_form_word(word, letter_count):
                word_score = get_word_score(word)
                for ch in word:
                    letter_count[ch] -= 1
                max_score = max(max_score, backtrack(index + 1, current_score + word_score, letter_count))
                for ch in word:
                    letter_count[ch] += 1
            
            return max_score
        
        letter_count = Counter(letters)
        return backtrack(0, 0, letter_count)

# Example usage
sol = Solution()
print(sol.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))  # Output: 23
print(sol.maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))  # Output: 27
print(sol.maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))  # Output: 0




