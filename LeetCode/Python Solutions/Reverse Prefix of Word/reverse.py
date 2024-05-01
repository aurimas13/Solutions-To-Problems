class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of ch
        index = word.find(ch)
        
        # If ch is not found, return the original word
        if index == -1:
            return word
        
        # Reverse the substring from start to index (inclusive) and concatenate with the rest
        return word[:index+1][::-1] + word[index+1:]
