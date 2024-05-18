/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private int moves;
    
    public int distributeCoins(TreeNode root) {
        moves = 0;
        dfs(root);
        return moves;
    }
    
    private int dfs(TreeNode node) {
        if (node == null) {
            return 0;
        }
        
        int leftExcess = dfs(node.left);
        int rightExcess = dfs(node.right);
        
        // Current node's total excess coins
        int excess = node.val + leftExcess + rightExcess - 1;
        
        // Total moves is the sum of the absolute values of excess coins from children
        moves += Math.abs(leftExcess) + Math.abs(rightExcess);
        
        return excess;
    }
}
