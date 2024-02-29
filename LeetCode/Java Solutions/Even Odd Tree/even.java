public class TreeNode {
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
    public boolean isEvenOddTree(TreeNode root) {
        if (root == null) {
            return false;
        }
        
        Queue<Pair<TreeNode, Integer>> queue = new LinkedList<>();
        queue.add(new Pair<>(root, 0));  // Node paired with its level
        
        while (!queue.isEmpty()) {
            Integer prevValue = null;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair<TreeNode, Integer> pair = queue.poll();
                TreeNode node = pair.getKey();
                int level = pair.getValue();
                
                if (level % 2 == 0) {  // Even level: values must be odd and strictly increasing
                    if (node.val % 2 == 0 || (prevValue != null && node.val <= prevValue)) {
                        return false;
                    }
                } else {  // Odd level: values must be even and strictly decreasing
                    if (node.val % 2 != 0 || (prevValue != null && node.val >= prevValue)) {
                        return false;
                    }
                }
                prevValue = node.val;
                
                if (node.left != null) {
                    queue.add(new Pair<>(node.left, level + 1));
                }
                if (node.right != null) {
                    queue.add(new Pair<>(node.right, level + 1));
                }
            }
        }
        
        return true;
    }
}
