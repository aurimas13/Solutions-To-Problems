class Solution {
    public boolean canArrange(int[] arr, int k) {
        int[] remainderCount = new int[k];
        
        for (int num : arr) {
            int remainder = ((num % k) + k) % k;  // Handle negative numbers
            remainderCount[remainder]++;
        }
        
        if (remainderCount[0] % 2 != 0) {
            return false;
        }
        
        for (int r = 1; r <= k / 2; r++) {
            if (r * 2 == k) {
                if (remainderCount[r] % 2 != 0) {
                    return false;
                }
            } else if (remainderCount[r] != remainderCount[k - r]) {
                return false;
            }
        }
        
        return true;
    }
}