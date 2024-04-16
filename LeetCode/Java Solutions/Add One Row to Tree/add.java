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
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }
        
        dfs(root, 1, val, depth);
        return root;
    }
    
    private void dfs(TreeNode node, int currentDepth, int val, int depth) {
        if (node == null) return;
        if (currentDepth == depth - 1) {
            TreeNode tempLeft = node.left;
            TreeNode tempRight = node.right;
            node.left = new TreeNode(val, tempLeft, null);
            node.right = new TreeNode(val, null, tempRight);
        } else {
            dfs(node.left, currentDepth + 1, val, depth);
            dfs(node.right, currentDepth + 1, val, depth);
        }
    }
}