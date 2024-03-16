class Solution {
    public int findMaxLength(int[] nums) {
        int max_length = 0;
        int running_sum = 0;
        HashMap<Integer, Integer> index_map = new HashMap<>();
        index_map.put(0, -1);  // Initialize with 0 sum at index -1
        
        for (int i = 0; i < nums.length; i++) {
            // Increment or decrement running_sum based on the value of num
            running_sum += nums[i] == 1 ? 1 : -1;
            
            // If this running_sum has been seen before, update max_length
            if (index_map.containsKey(running_sum)) {
                max_length = Math.max(max_length, i - index_map.get(running_sum));
            } else {
                // Store the first occurrence of this running_sum
                index_map.put(running_sum, i);
            }
        }
        
        return max_length;
    }
}
