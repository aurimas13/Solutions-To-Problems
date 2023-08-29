from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the minimum depth of a binary tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The minimum depth of the binary tree.
        """
        # If root is None (an empty tree), return 0 as there are no nodes.
        if root is None:
            return 0
        # If this node has no children, return 1.
        if root.left is None and root.right is None:
            return 1

        # If the left child is None, calculate min depth on the right subtree.
        if root.left is None:
            return self.minDepth(root.right) + 1
        # If the right child is None, calculate min depth on the left subtree.
        if root.right is None:
            return self.minDepth(root.left) + 1

        # If both children exist, calculate the min depth from both subtrees.
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
