# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val
            # Check if it's a leaf node
            if not node.left and not node.right:
                return current_sum
            # Recursively sum the numbers
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)