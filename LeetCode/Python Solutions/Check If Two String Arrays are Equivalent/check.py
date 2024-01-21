class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Concatenate all strings in word1
        concatenated_word1 = ''.join(word1)
        # Concatenate all strings in word2
        concatenated_word2 = ''.join(word2)

        # Compare the two concatenated strings
        return concatenated_word1 == concatenated_word2
