from collections import deque

class Solution:
    def largestValues(self, root):
        if not root:
            return []
        
        # Initialize the result list and the queue for level-order traversal
        result = []
        queue = deque([root])
        
        while queue:
            # Start the current level
            level_size = len(queue)
            max_value = float('-inf')  # Initialize the maximum value for this level
            
            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)  # Update the maximum value
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # After finishing the level, add the maximum value to the result list
            result.append(max_value)
        
        return result
