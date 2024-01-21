# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case
        if not root or root == p or root == q:
            return root

        x = self.lowestCommonAncestor(root.left, p, q)
        y = self.lowestCommonAncestor(root.right, p, q)

        if (x and y) or root in [p, q]:
            return root
        else:
            return x or y

# # Checking in terminal/console:
# if __name__ == '__main__':
#     Instant = Solution()
#     root = TreeNode(3)
#     root.left = TreeNode(5)
#     root.right = TreeNode(1)
#     root.left.left = TreeNode(6)
#     root.left.right = TreeNode(2)
#     root.right.left = TreeNode(0)
#     root.right.right = TreeNode(8)
#     # root.left.left.left = TreeNode()
#     # root.left.left.right = TreeNode()
#     root.left.right.left = TreeNode(7)
#     root.left.right.right = TreeNode(4)
#     Solve = Instant.lowestCommonAncestor(root, p = 5, q = 1) # root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1 -> 3
#     print(Solve)
