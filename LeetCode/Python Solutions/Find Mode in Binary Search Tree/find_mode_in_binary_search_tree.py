class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        self.prev_val = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if self.prev_val is None or self.prev_val != node.val:
                self.curr_count = 1
            else:
                self.curr_count += 1

            if self.curr_count == self.max_count:
                self.modes.append(node.val)
            elif self.curr_count > self.max_count:
                self.max_count = self.curr_count
                self.modes = [node.val]

            self.prev_val = node.val
            in_order(node.right)
            
        in_order(root)
        return self.modes
