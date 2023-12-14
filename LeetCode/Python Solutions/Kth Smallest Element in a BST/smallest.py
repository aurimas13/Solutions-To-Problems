from typing import List, Optional

class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        count = 0
        def visit(node):
            nonlocal ans, count
            if not node:
                return
            visit(node.left)
            count += 1
            if count == k:
                ans = node.val
            visit(node.right)
        visit(root)
        return ans


# Checking in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    # root.left.left = TreeNode()
    root.left.right = TreeNode(2)
    Solve = Instant.kthSmallest(root, k = 1) # root = [3,1,4,null,2], k = 1 -> 1
    print(Solve)
