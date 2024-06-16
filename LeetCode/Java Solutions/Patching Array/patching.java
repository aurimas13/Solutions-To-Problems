class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int i = 0;
        int patches = 0;
        
        while (miss <= n) {
            if (i < nums.length && nums[i] <= miss) {
                miss += nums[i];
                i++;
            } else {
                miss += miss;
                patches++;
            }
        }
        
        return patches;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.minPatches(new int[]{1, 3}, 6));  // Output: 1
        System.out.println(solution.minPatches(new int[]{1, 5, 10}, 20));  // Output: 2
        System.out.println(solution.minPatches(new int[]{1, 2, 2}, 5));  // Output: 0
    }
}
