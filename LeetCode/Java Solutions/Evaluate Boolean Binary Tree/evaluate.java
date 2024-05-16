# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # If the node is a leaf node, return its boolean value directly
        if root.val == 0:
            return False
        if root.val == 1:
            return True

        # Recursively evaluate the left and right children
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        # Apply the operation based on the node's value
        if root.val == 2:
            return left_val or right_val
        if root.val == 3:
            return left_val and right_val

        return False  # Default return (shouldn't reach here with valid inputs)

