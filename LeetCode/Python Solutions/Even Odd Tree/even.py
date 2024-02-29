class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        from collections import deque
        queue = deque([(root, 0)])  # Node paired with its level
        
        while queue:
            prev_value = None
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if level % 2 == 0:  # Even level: values must be odd and strictly increasing
                    if node.val % 2 == 0 or (prev_value is not None and node.val <= prev_value):
                        return False
                else:  # Odd level: values must be even and strictly decreasing
                    if node.val % 2 != 0 or (prev_value is not None and node.val >= prev_value):
                        return False
                prev_value = node.val
                
                if node.left:
                    queue.append((node.left, level + 1))
                if node.right:
                    queue.append((node.right, level + 1))
        
        return True
