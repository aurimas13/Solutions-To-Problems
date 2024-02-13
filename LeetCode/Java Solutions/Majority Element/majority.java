class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;
        
        for (int num : nums) {
            if (count == 0) {  // If count is 0, we choose the current number as the candidate.
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;  // Increment or decrement the count.
        }
        
        return candidate;  // The candidate is the majority element.
    }
}
