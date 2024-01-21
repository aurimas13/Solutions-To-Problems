class TreeNode:
    def __init__(self):
        self.next = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TreeNode()
            node = node.next[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._match(self.root, word, 0)

    def _match(self, node, word, index):
        if index == len(word):
            return node.is_word
        c = word[index]
        if c != ".":
            return c in node.next and self._match(node.next[c], word, index + 1)
        for n in node.next:
            if self._match(node.next[n], word, index + 1):
                return True
        return False
