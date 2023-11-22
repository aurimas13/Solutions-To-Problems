# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: if root is None, return False
        if root is None:
            return False
        
        # Check if the current tree is equal to the subtree
        if self.is_equal(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def is_equal(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        # Base cases: if both trees are None, return True
        if tree1 is None and tree2 is None:
            return True
        # If either tree is None, return False
        if tree1 is None or tree2 is None:
            return False
        
        # Check if the values of the trees are equal and recurse on left and right subtrees
        return (tree1.val == tree2.val) and self.is_equal(tree1.left, tree2.left) and self.is_equal(tree1.right, tree2.right)


if __name__ == '__main__':
    # Test cases
    solution = Solution()
    
    # Test case 1
    tree1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    tree2 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert solution.isSubtree(tree1, tree2) == True

    # Test case 2
    tree1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    tree2 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert solution.isSubtree(tree1, tree2) == False
