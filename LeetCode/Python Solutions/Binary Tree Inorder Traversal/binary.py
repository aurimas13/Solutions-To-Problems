class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, result):
            if node:
                inorder(node.left, result)
                result.append(node.val)
                inorder(node.right, result)
        
        result = []
        inorder(root, result)
        return result  
    
    