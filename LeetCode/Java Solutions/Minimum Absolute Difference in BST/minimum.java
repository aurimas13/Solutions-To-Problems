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

public class Solution {
    /**
     * This private method traverses a binary tree using inorder traversal and returns
     * a list of integers. If the root is null, an empty list is returned. The left and
     * right subtrees are traversed recursively and their results are merged.
     *
     * @param  root  the root node of the binary tree to be traversed
     * @return       a list of integers representing the inorder traversal of the tree
     */
    private List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<Integer>();
        }
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        left.add(root.val);
        left.addAll(right);
        return left;
    }
    
    /**
     * Calculates the minimum difference between any two nodes in a binary tree.
     *
     * @param  root  the root of the binary tree
     * @return       the minimum difference between any two nodes.
     */
    public int getMinimumDifference(TreeNode root) {
        List<Integer> values = inorderTraversal(root);
        int minDiff = Integer.MAX_VALUE;
        for (int i = 1; i < values.size(); i++) {
            minDiff = Math.min(minDiff, values.get(i) - values.get(i-1));
        }
        return minDiff;
    }
}
