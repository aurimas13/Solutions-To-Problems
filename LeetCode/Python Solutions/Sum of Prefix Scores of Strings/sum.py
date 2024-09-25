class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        
        # Build the Trie
        for word in words:
            self.insert(root, word)
        
        # Calculate prefix scores
        return [self.calculate_score(root, word) for word in words]
    
    def insert(self, node: TrieNode, word: str) -> None:
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def calculate_score(self, node: TrieNode, word: str) -> int:
        score = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            score += node.count
        return score