class Solution {
    public int specialArray(int[] nums) {
        // Sort the array in non-increasing order
        Arrays.sort(nums);
        
        int n = nums.length;
        
        // Loop through the possible values of x
        for (int x = 0; x <= n; x++) {
            int count = 0;
            for (int i = n - 1; i >= 0; i--) {
                if (nums[i] >= x) {
                    count++;
                } else {
                    break;
                }
            }
            if (count == x) {
                return x;
            }
        }
        
        // If x is not found, return -1
        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.specialArray(new int[]{3, 5}));  // Output: 2
        System.out.println(sol.specialArray(new int[]{0, 0}));  // Output: -1
        System.out.println(sol.specialArray(new int[]{0, 4, 3, 0, 4}));  // Output: 3
    }
}
