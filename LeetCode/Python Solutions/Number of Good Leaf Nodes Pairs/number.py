# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            # Check all combinations of left and right distances
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.result += 1
            
            # Increment all distances by 1 and return
            return [n + 1 for n in left_distances + right_distances]
        
        dfs(root)
        return self.result

# Example usage:
root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
sol = Solution()
print(sol.countPairs(root, 3))  # Output: 1
