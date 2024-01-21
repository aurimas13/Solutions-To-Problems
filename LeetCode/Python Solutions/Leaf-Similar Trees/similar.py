# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode) -> List[int]:
            # Base case: if the node is None; return empty list
            if not node:
                return []

            # if the node is a leaf (no left or right children), return its value in a list
            if not node.left and not node.right:
                return [node.val]
            
            # Recursively collect leaf values from left and right subtree
            return dfs(node.left) + dfs(node.right)

        return dfs(root1) == dfs(root2)