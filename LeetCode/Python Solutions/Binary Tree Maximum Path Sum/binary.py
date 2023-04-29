from typing import Optional
import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)

        self.max_sum = -sys.maxsize - 1
        dfs(root)
        return self.max_sum


# Checking in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    Solve = Instant.maxPathSum(root) # root = [1,2,3] -> 6
    print(Solve)
