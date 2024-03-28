class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        int left = 0, maxLength = 0;
        HashMap<Integer, Integer> freq = new HashMap<>();
        
        for (int right = 0; right < nums.length; right++) {
            // Update the frequency of the current right element
            freq.put(nums[right], freq.getOrDefault(nums[right], 0) + 1);
            
            // Shrink the window from the left if any frequency is greater than k
            while (freq.get(nums[right]) > k) {
                freq.put(nums[left], freq.get(nums[left]) - 1);
                if (freq.get(nums[left]) == 0) {
                    freq.remove(nums[left]);
                }
                left++;
            }
            
            // After ensuring no frequency is greater than k, calculate max length
            maxLength = Math.max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
}
