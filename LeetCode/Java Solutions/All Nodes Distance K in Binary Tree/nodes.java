import java.util.*;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode parent;  // Add parent pointer
    TreeNode(int x) { val = x; }
}

class Solution {
    /**
     * Returns a list of integers at distance k from the target node in a binary tree.
     *
     * @param  root    the root node of the binary tree
     * @param  target  the target node from which distance k is calculated
     * @param  k       the distance from the target node
     * @return         a list of integers at distance k from the target node
     */
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        // Function to add parent pointer to each node
        dfs(root, null);

        Queue<TreeNode> queue = new LinkedList<>();
        Set<TreeNode> seen = new HashSet<>();

        queue.offer(target);
        seen.add(target);
        int level = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();

            if (level == k) {
                List<Integer> res = new ArrayList<>();
                for (TreeNode node : queue) {
                    res.add(node.val);
                }
                return res;
            }

            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left != null && !seen.contains(node.left)) {
                    seen.add(node.left);
                    queue.offer(node.left);
                }
                if (node.right != null && !seen.contains(node.right)) {
                    seen.add(node.right);
                    queue.offer(node.right);
                }
                if (node.parent != null && !seen.contains(node.parent)) {
                    seen.add(node.parent);
                    queue.offer(node.parent);
                }
            }

            level++;
        }

        return new ArrayList<>();
    }

    private void dfs(TreeNode node, TreeNode parent) {
        if (node != null) {
            node.parent = parent;
            dfs(node.left, node);
            dfs(node.right, node);
        }
    }
}

