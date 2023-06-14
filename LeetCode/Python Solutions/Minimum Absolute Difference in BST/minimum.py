class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        Returns the minimum absolute difference of any two nodes in the given binary tree.
        :param root: A TreeNode representing the root of the binary tree.
        :type root: TreeNode
        :return: An integer representing the minimum absolute difference of any two nodes in the binary tree.
        :rtype: int
        """
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        values = inorder_traversal(root)
        return min(values[i+1] - values[i] for i in range(len(values)-1))
