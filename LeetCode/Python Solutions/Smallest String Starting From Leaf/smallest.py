# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.smallest = "~"  # Use a character lexicographically higher than 'z'

        def dfs(node, path):
            if node:
                # Prepend current character to path
                path = chr(node.val + ord('a')) + path
                # If it's a leaf node
                if not node.left and not node.right:
                    if path < self.smallest:
                        self.smallest = path
                else:
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, "")
        return self.smallest