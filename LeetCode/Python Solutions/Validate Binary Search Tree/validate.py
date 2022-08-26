# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.checkIfValid(root, -2 ** 32, 2 ** 32)

    def checkIfValid(self, root, minRange, maxRange):
        if not root:
            return True
        if minRange >= root.val or maxRange <= root.val:
            return False
        return self.checkIfValid(root.left, minRange, root.val) and self.checkIfValid(root.right, root.val, maxRange)


if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    Solve = Instant.isValidBST(root) # [2,1,3] -> true | root = TreeNode(5) -> root.left = TreeNode(1) -> root.right = TreeNode(4) -> root.left.left = TreeNode(None) -> root.left.right = TreeNode(None) -> root.right.left = TreeNode(3) -> root.right.right = TreeNode(6) -> root -> false
    print(Solve)
