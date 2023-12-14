from collections import deque
from typing import Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        """
        Given a binary tree, find the level which has the maximum sum of all nodes.
        If there are multiple levels with the same sum, return the smallest level.
        
        Args:
        - root: The root node of the binary tree
        
        Returns:
        - The level which has the maximum sum of all nodes
        
        Example:
        Input:
              1
             / \
            7   0
           / \
          7  -8
        Output: 2
        Explanation:
        Level 1 sum = 1
        Level 2 sum = 7 + 0 = 7
        Level 3 sum = 7 - 8 = -1
        So the level with the maximum sum is level 2.
        """
        if not root:
            return 0

        queue = deque([root])
        max_sum = float('-inf')
        max_level = 1
        level = 0

        while queue:
            size = len(queue)
            level += 1
            sum = 0

            for _ in range(size):
                node = queue.popleft()
                sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if sum > max_sum:
                max_sum = sum
                max_level = level

        return max_level
