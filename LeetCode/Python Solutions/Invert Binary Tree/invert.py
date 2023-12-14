from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = [root]
        while queue:
            node = queue.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.invertTree(TreeNode([4,2,7,1,3,6,9]))
    # root = [4,2,7,1,3,6,9] -> [4,7,2,9,6,3,1]
    print(Solve.val)
