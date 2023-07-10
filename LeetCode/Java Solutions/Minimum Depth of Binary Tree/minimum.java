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
    /**
     * Calculates the minimum depth of a binary tree.
     *
     * @param  root  the root node of the tree
     * @return       the minimum depth of the tree
     */
    public int minDepth(TreeNode root) {
        // If root is null (an empty tree), return 0 as there are no nodes.
        if (root == null) {
            return 0;
        }
        // If this node has no children, return 1.
        if (root.left == null && root.right == null) {
            return 1;
        }
        // If the left child is null, calculate min depth on the right subtree.
        if (root.left == null) {
            return minDepth(root.right) + 1;
        }
        // If the right child is null, calculate min depth on the left subtree.
        if (root.right == null) {
            return minDepth(root.left) + 1;
        }
        // If both children exist, calculate the min depth from both subtrees.
        return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
    }
}
