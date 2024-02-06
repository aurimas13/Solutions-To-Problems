class Solution {
    public int pseudoPalindromicPaths(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int path) {
        if (node == null) {
            return 0;
        }

        // Toggle the bit for the current node's value
        path ^= 1 << node.val;

        int count = 0;
        // If it's a leaf node, check if the path is pseudo-palindromic
        if (node.left == null && node.right == null) {
            count = (path & (path - 1)) == 0 ? 1 : 0;
        }

        // Continue DFS on left and right children
        return count + dfs(node.left, path) + dfs(node.right, path);
    }
}
