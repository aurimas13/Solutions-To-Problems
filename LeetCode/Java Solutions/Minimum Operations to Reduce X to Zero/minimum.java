import java.util.HashMap;

public class Solution {
    public int minOperations(int[] nums, int x) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        
        int target = total - x;
        if (target < 0) {
            return -1;
        }
        if (target == 0) {
            return nums.length;
        }
        
        HashMap<Integer, Integer> prefixSumIndex = new HashMap<>();
        prefixSumIndex.put(0, -1);
        int maxLength = Integer.MIN_VALUE;
        int currSum = 0;
        
        for (int i = 0; i < nums.length; i++) {
            currSum += nums[i];
            if (prefixSumIndex.containsKey(currSum - target)) {
                maxLength = Math.max(maxLength, i - prefixSumIndex.get(currSum - target));
            }
            prefixSumIndex.put(currSum, i);
        }
        
        return maxLength != Integer.MIN_VALUE ? nums.length - maxLength : -1;
    }
}
