import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {
    public int minOperations(int[] nums) {
        // Remove duplicates and sort the array
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        Integer[] sortedNums = set.toArray(new Integer[0]);
        Arrays.sort(sortedNums);
        
        // Use two pointers to represent a sliding window over the sorted array
        int l = 0, r = 0;
        int n = nums.length;
        int maxCount = 0;

        // Slide the window
        while (r < sortedNums.length) {
            // If the window is too large, reduce it from the left
            while (sortedNums[r] - sortedNums[l] >= n) {
                l++;
            }
            maxCount = Math.max(maxCount, r - l + 1);
            r++;
        }

        // Return the number of operations required
        return n - maxCount;
    }

    public static void main(String[] args) {
        Solution s = new Solution();

        // Test cases
        System.out.println(s.minOperations(new int[]{4,2,5,3}));  // 0
        System.out.println(s.minOperations(new int[]{1,2,3,5,6}));  // 1
        System.out.println(s.minOperations(new int[]{1,10,100,1000}));  // 3
    }
}
