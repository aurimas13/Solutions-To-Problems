class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:  # Traverse right first to ensure leftmost of the bottom is last
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val  # The last node processed will be the leftmost of the bottom



