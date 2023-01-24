from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        if left_depth == right_depth:
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            return (1 << right_depth) + self.countNodes(root.left)

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return 1 + self.depth(root.left)


# Checking in PyCharm/Console:
if __name__ == '__main__':
    Sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    Solve = Sol.countNodes(root)
    # root = [1,2,3,4,5,6] -> 6
    # root = [] -> 0
    # root = [1] -> 1
    print(Solve)
