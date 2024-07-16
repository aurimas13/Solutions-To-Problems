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
import java.util.*;

class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        Map<Integer, TreeNode> nodeMap = new HashMap<>();
        Set<Integer> children = new HashSet<>();

        // Create all nodes and establish parent-child relationships
        for (int[] description : descriptions) {
            int parent = description[0];
            int child = description[1];
            int isLeft = description[2];

            nodeMap.putIfAbsent(parent, new TreeNode(parent));
            nodeMap.putIfAbsent(child, new TreeNode(child));

            if (isLeft == 1) {
                nodeMap.get(parent).left = nodeMap.get(child);
            } else {
                nodeMap.get(parent).right = nodeMap.get(child);
            }

            children.add(child);
        }

        // Find the root node (it is the one that is not a child of any other node)
        TreeNode root = null;
        for (int[] description : descriptions) {
            int parent = description[0];
            if (!children.contains(parent)) {
                root = nodeMap.get(parent);
                break;
            }
        }

        return root;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] descriptions = {{20,15,1},{20,17,0},{50,20,1},{50,80,0},{80,19,1}};
        TreeNode root = sol.createBinaryTree(descriptions);
        // Further processing can be done on the 'root'
    }
}
