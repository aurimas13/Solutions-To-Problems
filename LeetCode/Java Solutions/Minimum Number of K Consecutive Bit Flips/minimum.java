class Solution {
    public int minKBitFlips(int[] nums, int k) {
        int n = nums.length;
        int flip = 0;
        int[] flipped = new int[n];
        int flipsCount = 0;

        for (int i = 0; i < n; i++) {
            if (i >= k) {
                flip ^= flipped[i - k];
            }
            if (nums[i] == flip) {
                if (i + k > n) {
                    return -1;
                }
                flip ^= 1;
                flipped[i] = 1;
                flipsCount += 1;
            }
        }

        return flipsCount;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.minKBitFlips(new int[]{0,1,0}, 1));  // Output: 2
        System.out.println(sol.minKBitFlips(new int[]{1,1,0}, 2));  // Output: -1
        System.out.println(sol.minKBitFlips(new int[]{0,0,0,1,0,1,1,0}, 3));  // Output: 3
    }
}
