class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.items = self._inorder()
        self.stack = [(self.root, False)]

    def _inorder(self):
        # Time: O(N), Space: O(h)
        stack = self.stack
        while stack:
            node, visited = stack.pop()
            if visited:
                yield node.val
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

    def next(self) -> int:
        # Time: O(1)
        return next(self.items)

    def hasNext(self) -> bool:
        # Time: O(1)
        return len(self.stack) > 0
