class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, path):
            if not node:
                return 0

            # Toggle the bit for the current node's value
            path ^= 1 << node.val
            
            # If it's a leaf node, check if the path is pseudo-palindromic
            count = 0
            if not node.left and not node.right:
                # Check if at most one bit is set in 'path'
                count = 1 if (path & (path - 1)) == 0 else 0
            
            # Continue DFS on left and right children
            return count + dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)
