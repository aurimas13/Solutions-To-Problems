class Trie:
    def __init__(self):
        self.root = {"": {}}

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current:
                next_node = {}
                current[char] = next_node
                current = next_node
            else:
                current = current[char]
        current[""] = {}

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current: return False
            current = current[char]
        return "" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current: return False
            current = current[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
