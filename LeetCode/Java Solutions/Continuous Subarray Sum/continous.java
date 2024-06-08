import java.util.HashMap;

class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        HashMap<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, -1);  // To handle case where the subarray starts from index 0
        int cumulativeSum = 0;
        
        for (int i = 0; i < nums.length; i++) {
            cumulativeSum += nums[i];
            if (k != 0) {  // Avoid division by zero
                cumulativeSum %= k;
            }
            
            if (remainderMap.containsKey(cumulativeSum)) {
                if (i - remainderMap.get(cumulativeSum) > 1) {
                    return true;
                }
            } else {
                remainderMap.put(cumulativeSum, i);
            }
        }
        
        return false;
    }

    // Example usage:
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.checkSubarraySum(new int[]{23, 2, 4, 6, 7}, 6));  // True
        System.out.println(sol.checkSubarraySum(new int[]{23, 2, 6, 4, 7}, 6));  // True
        System.out.println(sol.checkSubarraySum(new int[]{23, 2, 6, 4, 7}, 13)); // False
    }
}
