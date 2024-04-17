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
    private String smallest = "~";  // Use a character lexicographically higher than 'z'

    public String smallestFromLeaf(TreeNode root) {
        dfs(root, "");
        return smallest;
    }

    private void dfs(TreeNode node, String path) {
        if (node != null) {
            path = (char)(node.val + 'a') + path;  // Prepend character
            if (node.left == null && node.right == null) {  // Leaf node
                if (path.compareTo(smallest) < 0) {
                    smallest = path;
                }
            } else {
                dfs(node.left, path);
                dfs(node.right, path);
            }
        }
    }
}