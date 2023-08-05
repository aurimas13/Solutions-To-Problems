import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) return new ArrayList<>(); // If n is 0, return an empty list
        return generateTrees(1, n); // Call the recursive function to generate trees
    }

    private List<TreeNode> generateTrees(int start, int end) {
        List<TreeNode> trees = new ArrayList<>();
        if (start > end) {
            trees.add(null); // If start is greater than end, add null (base case)
            return trees;
        }

        // Iterate through all numbers from start to end
        for (int i = start; i <= end; i++) {
            List<TreeNode> leftTrees = generateTrees(start, i - 1); // Generate left subtrees
            List<TreeNode> rightTrees = generateTrees(i + 1, end); // Generate right subtrees

            // Combine left and right subtrees to form unique trees
            for (TreeNode left : leftTrees) {
                for (TreeNode right : rightTrees) {
                    TreeNode root = new TreeNode(i); // Create root with current value
                    root.left = left; // Assign left child
                    root.right = right; // Assign right child
                    trees.add(root); // Add the tree to the list
                }
            }
        }
        return trees;
    }
}

