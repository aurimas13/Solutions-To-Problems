import java.util.Arrays;

class Solution {
    public int maxDistance(int[] position, int m) {
        // Sort the positions to facilitate binary search
        Arrays.sort(position);
        
        // Function to check if it's possible to place m balls with at least minDist between them
        boolean canPlaceBalls(int[] position, int m, int minDist) {
            int count = 1;
            int lastPosition = position[0];
            for (int i = 1; i < position.length; i++) {
                if (position[i] - lastPosition >= minDist) {
                    count++;
                    lastPosition = position[i];
                    if (count == m) {
                        return true;
                    }
                }
            }
            return false;
        }
        
        // Binary search for the maximum minimum distance
        int low = 1;
        int high = position[position.length - 1] - position[0];
        int result = 0;
        
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canPlaceBalls(position, m, mid)) {
                result = mid;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.maxDistance(new int[]{1,2,3,4,7}, 3));  // Output: 3
        System.out.println(sol.maxDistance(new int[]{5,4,3,2,1,1000000000}, 2));  // Output: 999999999
    }
}
