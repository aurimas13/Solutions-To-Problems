class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def postOrder(node):
            if not node:
                return (0, 0)  # sum, count
            
            left_sum, left_count = postOrder(node.left)
            right_sum, right_count = postOrder(node.right)
            
            # Current sum and count including the current node
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # If the average of current subtree equals the node's value, increment the count
            if node.val == current_sum // current_count:
                self.count += 1
            
            return (current_sum, current_count)
        
        postOrder(root)
        return self.count
