class Solution {
    private int count = 0;

    public int averageOfSubtree(TreeNode root) {
        postOrder(root);
        return count;
    }

    private int[] postOrder(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0}; // sum, count
        }

        int[] left = postOrder(node.left);
        int[] right = postOrder(node.right);

        int currentSum = left[0] + right[0] + node.val;
        int currentCount = left[1] + right[1] + 1;

        if (node.val == currentSum / currentCount) {
            count++;
        }

        return new int[]{currentSum, currentCount};
    }
}
