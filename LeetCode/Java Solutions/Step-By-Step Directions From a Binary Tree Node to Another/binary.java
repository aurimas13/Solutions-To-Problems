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
    public String getDirections(TreeNode root, int startValue, int destValue) {
        StringBuilder pathToStart = new StringBuilder();
        StringBuilder pathToDest = new StringBuilder();
        
        // Helper function to find path from root to given value
        findPath(root, startValue, pathToStart);
        findPath(root, destValue, pathToDest);
        
        // Remove the common prefix path
        int i = 0;
        while (i < pathToStart.length() && i < pathToDest.length() && pathToStart.charAt(i) == pathToDest.charAt(i)) {
            i++;
        }
        
        StringBuilder result = new StringBuilder();
        for (int j = i; j < pathToStart.length(); j++) {
            result.append('U');
        }
        result.append(pathToDest.substring(i));
        
        return result.toString();
    }
    
    private boolean findPath(TreeNode root, int value, StringBuilder path) {
        if (root == null) {
            return false;
        }
        if (root.val == value) {
            return true;
        }
        path.append('L');
        if (findPath(root.left, value, path)) {
            return true;
        }
        path.deleteCharAt(path.length() - 1);
        
        path.append('R');
        if (findPath(root.right, value, path)) {
            return true;
        }
        path.deleteCharAt(path.length() - 1);
        
        return false;
    }
}

// Example usage:
// TreeNode root = new TreeNode(5, new TreeNode(1, new TreeNode(3), null), new TreeNode(2, new TreeNode(6), new TreeNode(4)));
// Solution sol = new Solution();
// System.out.println(sol.getDirections(root, 3, 6));  // Output: "UURL"
