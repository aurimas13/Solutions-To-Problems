import java.util.ArrayList;
import java.util.List;

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
    int result = 0;
    
    public int countPairs(TreeNode root, int distance) {
        dfs(root, distance);
        return result;
    }
    
    private List<Integer> dfs(TreeNode node, int distance) {
        if (node == null) {
            return new ArrayList<>();
        }
        if (node.left == null && node.right == null) {
            List<Integer> leafDistance = new ArrayList<>();
            leafDistance.add(1);
            return leafDistance;
        }
        
        List<Integer> leftDistances = dfs(node.left, distance);
        List<Integer> rightDistances = dfs(node.right, distance);
        
        for (int l : leftDistances) {
            for (int r : rightDistances) {
                if (l + r <= distance) {
                    result++;
                }
            }
        }
        
        List<Integer> currentDistances = new ArrayList<>();
        for (int l : leftDistances) {
            if (l + 1 <= distance) {
                currentDistances.add(l + 1);
            }
        }
        for (int r : rightDistances) {
            if (r + 1 <= distance) {
                currentDistances.add(r + 1);
            }
        }
        return currentDistances;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.right = new TreeNode(4);
        root.right = new TreeNode(3);

        System.out.println(sol.countPairs(root, 3));  // Output: 1
    }
}
