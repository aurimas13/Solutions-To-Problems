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
    private int sum = 0;

    public TreeNode bstToGst(TreeNode root) {
        // Perform a reverse in-order traversal
        traverse(root);
        return root;
    }

    private void traverse(TreeNode node) {
        if (node == null) {
            return;
        }
        // Traverse the right subtree first
        traverse(node.right);

        // Process the current node
        sum += node.val;
        node.val = sum;

        // Traverse the left subtree
        traverse(node.left);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        // Example usage:
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(1);
        root.right = new TreeNode(6);
        root.left.left = new TreeNode(0);
        root.left.right = new TreeNode(2);
        root.left.right.right = new TreeNode(3);
        root.right.left = new TreeNode(5);
        root.right.right = new TreeNode(7);
        root.right.right.right = new TreeNode(8);

        TreeNode result = sol.bstToGst(root);

        // Print the resulting GST (you can implement a print method to check the results)
    }
}
