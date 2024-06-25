# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.sum = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root
    
    def traverse(self, node: TreeNode):
        if not node:
            return
        # Traverse the right subtree first
        self.traverse(node.right)
        
        # Process the current node
        self.sum += node.val
        node.val = self.sum
        
        # Traverse the left subtree
        self.traverse(node.left)

# Example usage:
# sol = Solution()
# root = TreeNode(4)
# root.left = TreeNode(1)
# root.right = TreeNode(6)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(2)
# root.left.right.right = TreeNode(3)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(8)

# result = sol.bstToGst(root)
# You can implement a print method to check the results
