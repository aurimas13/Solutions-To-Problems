import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

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
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<Integer> toDeleteSet = new HashSet<>();
        for (int val : to_delete) {
            toDeleteSet.add(val);
        }
        List<TreeNode> remainingForest = new ArrayList<>();
        
        helper(root, true, toDeleteSet, remainingForest);
        return remainingForest;
    }
    
    private TreeNode helper(TreeNode node, boolean isRoot, Set<Integer> toDeleteSet, List<TreeNode> remainingForest) {
        if (node == null) {
            return null;
        }
        boolean rootDeleted = toDeleteSet.contains(node.val);
        if (isRoot && !rootDeleted) {
            remainingForest.add(node);
        }
        node.left = helper(node.left, rootDeleted, toDeleteSet, remainingForest);
        node.right = helper(node.right, rootDeleted, toDeleteSet, remainingForest);
        return rootDeleted ? null : node;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        TreeNode root = new TreeNode(1, 
            new TreeNode(2, new TreeNode(4), new TreeNode(5)), 
            new TreeNode(3, new TreeNode(6), new TreeNode(7))
        );
        List<TreeNode> result = sol.delNodes(root, new int[]{3, 5});
        for (TreeNode tree : result) {
            // print the roots of the remaining forest
            System.out.println(tree.val);
        }
    }
}


