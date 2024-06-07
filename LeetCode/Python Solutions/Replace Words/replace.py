from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search_root(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                return word
            node = node.children[char]
            prefix += char
            if node.is_word:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            trie.insert(root)
        
        words = sentence.split()
        result = []
        for word in words:
            result.append(trie.search_root(word))
        
        return " ".join(result)

# Example usage:
sol = Solution()
print(sol.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))  # Output: "the cat was rat by the bat"
print(sol.replaceWords(["a","b","c"], "aadsfasf absbs bbab cadsfafs"))  # Output: "a a b c"
