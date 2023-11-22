class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [] # If n is 0, return an empty list
        return self.generate_trees(1, n) # Call the recursive function to generate trees

    def generate_trees(self, start, end):
        trees = []
        if start > end:
            trees.append(None) # If start is greater than end, add None (base case)
            return trees

        # Iterate through all numbers from start to end
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1) # Generate left subtrees
            right_trees = self.generate_trees(i + 1, end) # Generate right subtrees

            # Combine left and right subtrees to form unique trees
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i) # Create root with current value
                    root.left = left # Assign left child
                    root.right = right # Assign right child
                    trees.append(root) # Add the tree to the list

        return trees
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [] # If n is 0, return an empty list
        return self.generate_trees(1, n) # Call the recursive function to generate trees

    def generate_trees(self, start, end):
        trees = []
        if start > end:
            trees.append(None) # If start is greater than end, add None (base case)
            return trees

        # Iterate through all numbers from start to end
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1) # Generate left subtrees
            right_trees = self.generate_trees(i + 1, end) # Generate right subtrees

            # Combine left and right subtrees to form unique trees
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i) # Create root with current value
                    root.left = left # Assign left child
                    root.right = right # Assign right child
                    trees.append(root) # Add the tree to the list

        return trees
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return [] # If n is 0, return an empty list
        return self.generate_trees(1, n) # Call the recursive function to generate trees

    def generate_trees(self, start, end):
        trees = []
        if start > end:
            trees.append(None) # If start is greater than end, add None (base case)
            return trees

        # Iterate through all numbers from start to end
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1) # Generate left subtrees
            right_trees = self.generate_trees(i + 1, end) # Generate right subtrees

            # Combine left and right subtrees to form unique trees
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i) # Create root with current value
                    root.left = left # Assign left child
                    root.right = right # Assign right child
                    trees.append(root) # Add the tree to the list

        return trees

