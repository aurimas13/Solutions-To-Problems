# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Step 1: Perform in-order traversal to collect nodes in sorted order
        nodes = []
        self.inorder(root, nodes)
        
        # Step 2: Build balanced BST from sorted nodes
        return self.build_balanced_bst(nodes, 0, len(nodes) - 1)
    
    def inorder(self, node, nodes):
        if not node:
            return
        self.inorder(node.left, nodes)
        nodes.append(node)
        self.inorder(node.right, nodes)
    
    def build_balanced_bst(self, nodes, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.build_balanced_bst(nodes, start, mid - 1)
        root.right = self.build_balanced_bst(nodes, mid + 1, end)
        return root

# Example usage:
# root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
# sol = Solution()
# balanced_root = sol.balanceBST(root)
