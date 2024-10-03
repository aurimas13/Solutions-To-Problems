import java.util.*;

class Solution {
    public int minSubarray(int[] nums, int p) {
        int n = nums.length;
        long totalSum = 0;
        for (int num : nums) {
            totalSum += num;
        }
        
        int target = (int) (totalSum % p);
        if (target == 0) return 0;
        
        Map<Integer, Integer> prefixSumMod = new HashMap<>();
        prefixSumMod.put(0, -1);
        int currentSum = 0;
        int minLength = n;
        
        for (int i = 0; i < n; i++) {
            currentSum = (currentSum + nums[i]) % p;
            int complement = (currentSum - target + p) % p;
            
            if (prefixSumMod.containsKey(complement)) {
                minLength = Math.min(minLength, i - prefixSumMod.get(complement));
            }
            
            prefixSumMod.put(currentSum, i);
        }
        
        return minLength < n ? minLength : -1;
    }
}