# Importing typing module to define List and Optional
from typing import List, Optional

# Defining the binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Create a memoization dictionary to store solutions for each 'n' to avoid recalculations
        memo = {0: [], 1: [TreeNode(0)]}

        def helper(n):
            # If 'n' is in memo, return memo[n] immediately
            if n in memo:
                return memo[n]
            
            # Create an empty list to store all possible trees
            ans = []
            
            # A full binary tree of 'n' nodes is a combination of all possible full binary trees of 'x' nodes on the left and 'n-x-1' nodes on the right
            for x in range(1, n, 2):
                # Get all possible full binary trees on the left
                for left in helper(x):
                    # Get all possible full binary trees on the right
                    for right in helper(n - x - 1):
                        # Create a new full binary tree with the left and right subtrees
                        ans.append(TreeNode(0, left, right))

            # Store the answer in memo and return it
            memo[n] = ans
            return ans

        # Call the helper function
        return helper(n)


