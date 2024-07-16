# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_map = {}
        children = set()

        # Create all nodes and establish parent-child relationships
        for parent, child, is_left in descriptions:
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            if child not in node_map:
                node_map[child] = TreeNode(child)
            
            if is_left:
                node_map[parent].left = node_map[child]
            else:
                node_map[parent].right = node_map[child]
            
            children.add(child)

        # Find the root node (it is the one that is not a child of any other node)
        root = None
        for parent, _, _ in descriptions:
            if parent not in children:
                root = node_map[parent]
                break

        return root

# Example usage:
sol = Solution()
descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
root = sol.createBinaryTree(descriptions)
