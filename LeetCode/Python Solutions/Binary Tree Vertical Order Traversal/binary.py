from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Initialize a dictionary to store the columns and their corresponding values
        columns = {}

        # Initialize a deque for breadth-first search
        queue = deque([(root, 0)])  # (node, column)

        while queue:
            node, col = queue.popleft()
            if col not in columns:
                columns[col] = [node.val]
            else:
                columns[col].append(node.val)

            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))

        # sort the columns by their keys
        sorted_columns = sorted(columns.items())
        result = [col[1] for col in sorted_columns]
        return result


# Checking in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(8)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(0)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(7)
    Solve = Instant.verticalOrder(root)
    # root = [3,9,8,4,0,1,7] -> [[4],[9],[3,0,1],[8],[7]]
    print(Solve)
