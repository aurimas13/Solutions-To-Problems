import java.util.HashMap;

class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        // HashMap to store the frequency of prefix sum remainders
        HashMap<Integer, Integer> remainderMap = new HashMap<>();
        remainderMap.put(0, 1); // Initial condition: prefix sum of 0 with frequency 1
        
        int cumulativeSum = 0;
        int count = 0;

        for (int num : nums) {
            cumulativeSum += num;
            
            // Compute the remainder of cumulativeSum when divided by k
            int remainder = cumulativeSum % k;
            // Adjust remainder to be positive (Java handles negative remainders differently)
            if (remainder < 0) {
                remainder += k;
            }
            
            // If this remainder has been seen before, it contributes to the count
            if (remainderMap.containsKey(remainder)) {
                count += remainderMap.get(remainder);
            }
            
            // Update the frequency of this remainder in the map
            remainderMap.put(remainder, remainderMap.getOrDefault(remainder, 0) + 1);
        }

        return count;
    }
    
    // Example usage:
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.subarraysDivByK(new int[]{4, 5, 0, -2, -3, 1}, 5));  // 7
        System.out.println(sol.subarraysDivByK(new int[]{5}, 9));  // 0
    }
}
