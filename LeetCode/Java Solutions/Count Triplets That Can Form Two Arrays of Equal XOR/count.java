class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        int[] prefix = new int[n + 1];
        
        // Compute the prefix XOR array
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] ^ arr[i - 1];
        }
        
        int count = 0;
        
        // Find valid (i, j, k) triplets
        for (int i = 0; i < n; i++) {
            for (int k = i + 1; k < n; k++) {
                if (prefix[i] == prefix[k + 1]) {
                    count += (k - i);
                }
            }
        }
        
        return count;
    }

    // Test cases
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countTriplets(new int[]{2, 3, 1, 6, 7}));  // Output: 4
        System.out.println(sol.countTriplets(new int[]{1, 1, 1, 1, 1}));  // Output: 10
    }
}
