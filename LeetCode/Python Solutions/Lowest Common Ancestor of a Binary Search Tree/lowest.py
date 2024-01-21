from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        if p.val>q.val:
            p,q=q,p
        while True:
            if p.val<=node.val<=q.val:
                return node
            if p.val>node.val:
                node=node.right
            else:
                node=node.left


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.right.right.left = TreeNode(None)
    root.right.right.right = TreeNode(None)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    Solve = Instant.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)) #  root representing a list of [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8 -> 6
    print(Solve.val)
