import java.util.Queue;
import java.util.LinkedList;

/**
 * Definition for a binary tree node.
 */
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

public class Solution {
/**
 * Returns the level of the binary tree with the maximum sum of values of its nodes. 
 * If there are multiple levels with the same sum, returns the level closest to the root.
 *
 * @param  root  the root node of the binary tree
 * @return       the level of the binary tree with the maximum sum of values
 *               of its nodes
 */
public int maxLevelSum(TreeNode root) {
    // if the root is null, return 0
    if (root == null) {
        return 0;
    }
    
    // initialize a queue with the root node
    Queue<TreeNode> queue = new LinkedList<>();
    queue.offer(root);
    
    // initialize variables to keep track of maximum sum, maximum level, and current level
    int maxSum = Integer.MIN_VALUE;
    int maxLevel = 1;
    int level = 0;
    
    // loop through the binary tree using a queue
    while (!queue.isEmpty()) {
        // get the number of nodes in the current level
        int size = queue.size();
        // initialize a variable to keep track of the sum of the nodes in the current level
        int sum = 0;
        // increment the level counter
        level++;
        
        // loop through the nodes in the current level
        for (int i = 0; i < size; i++) {
            // get the next node in the queue
            TreeNode node = queue.poll();
            // add the node's value to the sum
            sum += node.val;
            
            // add the node's left and right children to the queue if they exist
            if (node.left != null) {
                queue.offer(node.left);
            }
            
            if (node.right != null) {
                queue.offer(node.right);
            }
        }
        
        // update the maximum sum and maximum level if the current sum is greater than the current maximum sum
        if (sum > maxSum) {
            maxSum = sum;
            maxLevel = level;
        }
    }
    
    // return the level with the maximum sum
    return maxLevel;
}

    public static void main(String[] args) {
        // Example usage
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(7, new TreeNode(7), null);
        root.right = new TreeNode(0, null, new TreeNode(-8));
        
        Solution solution = new Solution();
        System.out.println(solution.maxLevelSum(root)); // Output should be 2
    }
}
