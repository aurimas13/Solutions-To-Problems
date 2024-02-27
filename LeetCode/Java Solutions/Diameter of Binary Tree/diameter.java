/**
 * Definition for a binary tree node.
 */
public class TreeNode {
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
    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        depth(root);
        return maxDiameter;
    }
    
    private int depth(TreeNode node) {
        if (node == null) {
            return 0;
        }
        // Recursively find the depth of the left and right subtrees
        int leftDepth = depth(node.left);
        int rightDepth = depth(node.right);
        // Update the maximum diameter with the sum of left and right depths at this node
        maxDiameter = Math.max(maxDiameter, leftDepth + rightDepth);
        // Return the depth of this subtree
        return 1 + Math.max(leftDepth, rightDepth);
    }
}
