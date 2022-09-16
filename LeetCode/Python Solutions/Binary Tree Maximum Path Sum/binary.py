from typing import List, Optional
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.largest = -sys.maxsize
        self.dfs(root)
        return self.largest

    def dfs(self, root):
        if root is None:
            return 0
        left_single_max = self.dfs(root.left)
        right_single_max = self.dfs(root.right)

        single_max = max(root.val, left_single_max + root.val, right_single_max + root.val)
        self.largest = max(self.largest, single_max, root.val + left_single_max + right_single_max)
        return single_max


# Checking in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    Solve = Instant.maxPathSum(root) # root = [1,2,3] -> 6
    print(Solve)
