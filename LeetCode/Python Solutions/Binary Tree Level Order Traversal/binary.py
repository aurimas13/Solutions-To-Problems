from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        from collections import deque
        from collections import defaultdict

        q = deque([(root, 0)])
        level_order = defaultdict(list)

        while q:
            node, level = q.popleft()
            level_order[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return level_order.values()


# Checking in terminal/console:
if __name__ == '__main__':
    Instant = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    # root.left.left = TreeNode()
    # root.left.right = TreeNode()
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    Solve = Instant.levelOrder(root) # root = [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]
    print(Solve)
