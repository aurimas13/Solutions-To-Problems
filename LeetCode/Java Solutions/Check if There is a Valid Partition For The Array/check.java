import java.util.HashMap;

public class Solution {
    private int[] nums;
    private HashMap<Integer, Boolean> memo;

    public boolean validPartition(int[] nums) {
        this.nums = nums;
        this.memo = new HashMap<>();
        return canPartitionFrom(0);
    }

    private boolean canPartitionFrom(int index) {
        if (index == nums.length) {
            return true;
        }

        if (memo.containsKey(index)) {
            return memo.get(index);
        }

        // Check for a pair of equal numbers
        if (index + 1 < nums.length && nums[index] == nums[index + 1] && canPartitionFrom(index + 2)) {
            memo.put(index, true);
            return true;
        }

        // Check for a triplet of equal numbers
        if (index + 2 < nums.length && nums[index] == nums[index + 1] && nums[index] == nums[index + 2] && canPartitionFrom(index + 3)) {
            memo.put(index, true);
            return true;
        }

        // Check for a triplet of consecutive numbers
        if (index + 2 < nums.length && nums[index] + 1 == nums[index + 1] && nums[index + 1] + 1 == nums[index + 2] && canPartitionFrom(index + 3)) {
            memo.put(index, true);
            return true;
        }

        memo.put(index, false);
        return false;
    }
}

