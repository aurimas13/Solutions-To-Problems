// Importing necessary libraries
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    // Create a memoization array to store solutions for each 'n' to avoid recalculations
    Map<Integer, List<TreeNode>> memo = new HashMap<>() {{ put(0, new ArrayList<>()); put(1, Arrays.asList(new TreeNode(0))); }};
    
    public List<TreeNode> allPossibleFBT(int n) {
        // If 'n' is in memo, return memo.get(n) immediately
        if (memo.containsKey(n)) {
            return memo.get(n);
        }

        // Create an empty list to store all possible trees
        List<TreeNode> ans = new ArrayList<>();
        
        // A full binary tree of 'n' nodes is a combination of all possible full binary trees of 'x' nodes on the left and 'n-x-1' nodes on the right
        for (int x = 1; x < n; x += 2) {
            // Get all possible full binary trees on the left
            for (TreeNode left : allPossibleFBT(x)) {
                // Get all possible full binary trees on the right
                for (TreeNode right : allPossibleFBT(n - x - 1)) {
                    // Create a new full binary tree with the left and right subtrees
                    ans.add(new TreeNode(0, left, right));
                }
            }
        }
        
        // Store the answer in memo and return it
        memo.put(n, ans);
        return ans;
    }
}

