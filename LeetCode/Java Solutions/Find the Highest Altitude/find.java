public class Solution {
    public int largestAltitude(int[] gain) {
        int altitude = 0;  // Initialize altitude to 0
        int maxAltitude = 0;  // Initialize maxAltitude to 0
        
        // Iterate through each gain
        for (int g : gain) {
            altitude += g;  // Add gain to current altitude
            maxAltitude = Math.max(maxAltitude, altitude);  // Update maxAltitude if current altitude is greater
        }
        
        // Return the max altitude
        return maxAltitude;
    }
    
    public static void main(String[] args) {
        // Sample usage
        Solution solution = new Solution();
        System.out.println(solution.largestAltitude(new int[]{-5, 1, 5, 0, -7}));  // Output: 1
        System.out.println(solution.largestAltitude(new int[]{-4, -3, -2, -1, 4, 3, 2}));  // Output: 0
    }
}
