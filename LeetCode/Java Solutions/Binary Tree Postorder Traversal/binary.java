class Solution {
    private List<Integer> result = new ArrayList<>();
    
    public List<Integer> postorderTraversal(TreeNode root) {
        postorder(root);
        return result;
    }
    
    private void postorder(TreeNode node) {
        if (node == null) return;
        postorder(node.left);
        postorder(node.right);
        result.add(node.val);
    }
}