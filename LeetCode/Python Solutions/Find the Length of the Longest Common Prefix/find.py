class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()
        
        # Insert all numbers from arr1 into the Trie
        for num in arr1:
            self.insert(root, str(num))
        
        max_prefix = 0
        
        # Check for common prefixes with numbers from arr2
        for num in arr2:
            max_prefix = max(max_prefix, self.find_longest_prefix(root, str(num)))
        
        return max_prefix
    
    def insert(self, node: TrieNode, num: str) -> None:
        for digit in num:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
            node.count += 1
    
    def find_longest_prefix(self, node: TrieNode, num: str) -> int:
        length = 0
        for digit in num:
            if digit not in node.children or node.children[digit].count == 0:
                break
            node = node.children[digit]
            length += 1
        return length