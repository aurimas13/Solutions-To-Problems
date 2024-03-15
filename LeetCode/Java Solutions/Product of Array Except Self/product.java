class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        
        // Calculate the product of all elements to the left of each element
        int left_product = 1;
        for (int i = 0; i < n; i++) {
            answer[i] = left_product;
            left_product *= nums[i];
        }
        
        // Calculate the product of all elements to the right of each element
        // and multiply it by the product calculated in the previous step
        int right_product = 1;
        for (int i = n - 1; i >= 0; i--) {
            answer[i] *= right_product;
            right_product *= nums[i];
        }
        
        return answer;
    }
}
