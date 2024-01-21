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
    public int rangeSumBST(TreeNode root, int low, int high) {
        if (root == null) {  // If the node is null, return 0
            return 0;
        }
        
        if (root.val < low) {  // If the value is less than low, only consider the right subtree
            return rangeSumBST(root.right, low, high);
        }
        
        if (root.val > high) {  // If the value is greater than high, only consider the left subtree
            return rangeSumBST(root.left, low, high);
        }
        
        // If the value is within the range, include it and continue to both subtrees
        return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high);
    }
}
