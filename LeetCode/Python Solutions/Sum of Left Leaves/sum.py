# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        def dfs(node):
            if not node:
                return 0
            
            left_sum = 0
            if node.left and isLeaf(node.left):
                left_sum = node.left.val
            return left_sum + dfs(node.left) + dfs(node.right)
        
        return dfs(root)