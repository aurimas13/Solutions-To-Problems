import java.util.ArrayList;
import java.util.List;

class Solution {
    private Integer prevVal = null;
    private int currCount = 0;
    private int maxCount = 0;
    private List<Integer> modes = new ArrayList<>();

    public int[] findMode(TreeNode root) {
        if (root == null) {
            return new int[0];
        }

        inOrder(root);

        int[] result = new int[modes.size()];
        for (int i = 0; i < modes.size(); i++) {
            result[i] = modes.get(i);
        }
        return result;
    }

    private void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }

        inOrder(node.left);

        if (prevVal == null || !prevVal.equals(node.val)) {
            currCount = 1;
        } else {
            currCount++;
        }

        if (currCount == maxCount) {
            modes.add(node.val);
        } else if (currCount > maxCount) {
            maxCount = currCount;
            modes.clear();
            modes.add(node.val);
        }

        prevVal = node.val;

        inOrder(node.right);
    }
}
