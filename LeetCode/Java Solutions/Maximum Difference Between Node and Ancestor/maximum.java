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
    public int maxAncestorDiff(TreeNode root) {
        return dfs(root, root.val, root.val);
    }

    private int dfs(TreeNode node, int minVal, int maxVal) {
        if (node == null) {
            return maxVal - minVal;
        }
        maxVal = Math.max(maxVal, node.val);
        minVal = Math.min(minVal, node.val);
        int leftDiff = dfs(node.left, minVal, maxVal);
        int rightDiff = dfs(node.right, minVal, maxVal);
        return Math.max(leftDiff, rightDiff);
    }
}
