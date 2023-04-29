from typing import Optional
from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            total_paths = path_sums[current_sum - targetSum]
            path_sums[current_sum] += 1

            total_paths += dfs(node.left, current_sum)
            total_paths += dfs(node.right, current_sum)

            path_sums[current_sum] -= 1
            return total_paths

        path_sums = defaultdict(int)
        path_sums[0] = 1
        return dfs(root, 0)
    

# Write some test cases for your solution 
 if __name__ == "__main__":
    def test_pathSum(): 
        """ 
        Tests for pathSum function 
        """
        solution = Solution()
        assert solution.pathSum([10,5,-3,3,2,null,11,3,-2,null,1], 8) == 3
        assert solution.pathSum([5,4,8,11,null,13,4,7,2,null,null,5,1], 22) == 3
        assert solution.pathSum([1,2,3], 5) == 0
        assert solution.pathSum([1,2], 0) == 0  
        assert solution.pathSum([1,2,3,4,5,6,7,8,9,10], 15) == 2
        assert solution.pathSum([1,2,3,4,5,6,7,8,9,10,11,12,13], 15) == 2        

    test_pathSum()
    print("All tests passed successfully.")