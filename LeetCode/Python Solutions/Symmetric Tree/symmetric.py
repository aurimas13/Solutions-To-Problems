from collections import deque
from typing import Optional


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSymmetric(root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            left = q.popleft()
            right = q.popleft()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            q.append(left.left)
            q.append(right.right)
            q.append(left.right)
            q.append(right.left)
        return True


# Running in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    Solve = Instant.isSymmetric(root = TreeNode([1, 2, 2, 3, 4, 4, 3]))
    # root = TreeNode([1,2,2,3,4,4,3]) -> true
    # root = TreeNode([1,2,2,null,3,null,3]) -> false
    print(Solve)
