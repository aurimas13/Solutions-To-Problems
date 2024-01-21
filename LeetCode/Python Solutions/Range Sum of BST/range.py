# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:  # If the node is None, return 0
            return 0
        
        if root.val < low:  # If the value is less than low, only consider the right subtree
            return self.rangeSumBST(root.right, low, high)
        
        if root.val > high:  # If the value is greater than high, only consider the left subtree
            return self.rangeSumBST(root.left, low, high)
        
        # If the value is within the range, include it and continue to both subtrees
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
