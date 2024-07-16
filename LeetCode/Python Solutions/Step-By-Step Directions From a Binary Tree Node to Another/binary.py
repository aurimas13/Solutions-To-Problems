# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        # Helper function to find path from root to given value
        def findPath(root, value, path):
            if not root:
                return False
            if root.val == value:
                return True
            path.append('L')
            if findPath(root.left, value, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, value, path):
                return True
            path.pop()
            return False
        
        # Find the paths from root to startValue and destValue
        path_to_start, path_to_dest = [], []
        findPath(root, startValue, path_to_start)
        findPath(root, destValue, path_to_dest)
        
        # Remove the common prefix path
        i = 0
        while i < len(path_to_start) and i < len(path_to_dest) and path_to_start[i] == path_to_dest[i]:
            i += 1
        return 'U' * (len(path_to_start) - i) + ''.join(path_to_dest[i:])

# Example usage:
root = TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4)))
sol = Solution()
print(sol.getDirections(root, 3, 6))  # Output: "UURL"
