from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)
        
        queue = [(target, 0)]
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            node, d = queue.pop(0)
            for n in (node.left, node.right, node.parent):
                if n and n not in seen:
                    seen.add(n)
                    queue.append((n, d+1))
        return []
    

    # Driver Code
    if __name__ == "__main__":
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        target = root.left
        k = 2
        print(Solution.distanceK(root, target, k))
