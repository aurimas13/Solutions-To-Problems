import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) {
            return result;
        }

        // Initialize the queue for level-order traversal
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            int max = Integer.MIN_VALUE;  // Initialize the maximum value for this level

            // Process all nodes in the current level
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                max = Math.max(max, node.val);  // Update the maximum value

                // Add children to the queue for the next level
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            // After finishing the level, add the maximum value to the result list
            result.add(max);
        }

        return result;
    }
}
