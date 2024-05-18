# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            
            # Current node's total excess coins
            excess = node.val + left_excess + right_excess - 1
            
            # Total moves is the sum of the absolute values of excess coins from children
            self.moves += abs(left_excess) + abs(right_excess)
            
            return excess
        
        dfs(root)
        return self.moves
