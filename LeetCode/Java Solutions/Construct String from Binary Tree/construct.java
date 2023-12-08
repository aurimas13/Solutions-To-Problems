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
    public String tree2str(TreeNode root) {
        if (root == null) {
            return "";
        }
        
        // Process the root node
        StringBuilder result = new StringBuilder();
        result.append(root.val);
        
        // Process the left subtree
        if (root.left != null || root.right != null) {
            result.append("(").append(tree2str(root.left)).append(")");
        }
        
        // Process the right subtree
        if (root.right != null) {
            result.append("(").append(tree2str(root.right)).append(")");
        }
        
        return result.toString();
    }
}